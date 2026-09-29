"""N-gram language models implemented from counts only.

This module intentionally does not use an existing language-model package.  It
implements vocabulary construction, n-gram counting, MLE/Laplace probability,
sentence log-probability, perplexity, next-word prediction, and continuation
scoring directly with ``collections.Counter``.
"""

from __future__ import annotations

import math
from collections import Counter
from typing import Iterable, Iterator, Sequence


BOS = "<s>"
EOS = "</s>"
UNK = "<unk>"


def build_vocabulary(
    corpus: Iterable[Sequence[str]],
    min_count: int = 2,
    max_size: int | None = 50_000,
) -> set[str]:
    """Build a training-only vocabulary.

    Tokens below ``min_count`` or beyond ``max_size`` are represented by
    ``<unk>``. ``</s>`` is predicted by the model; ``<s>`` is context-only.
    """
    if min_count < 1:
        raise ValueError("min_count must be at least 1")
    counts = Counter(token for sentence in corpus for token in sentence)
    ordered = [
        token
        for token, count in counts.most_common()
        if count >= min_count and token not in {BOS, EOS, UNK}
    ]
    if max_size is not None:
        if max_size < 2:
            raise ValueError("max_size must leave room for </s> and <unk>")
        ordered = ordered[: max_size - 2]
    return set(ordered) | {EOS, UNK}


def count_ngrams(
    corpus: Iterable[Sequence[str]],
    n: int,
    vocabulary: set[str],
) -> tuple[Counter[tuple[str, ...]], Counter[tuple[str, ...]]]:
    """Count n-grams and their contexts in a tokenized corpus."""
    if n < 1:
        raise ValueError("n must be at least 1")

    ngram_counts: Counter[tuple[str, ...]] = Counter()
    context_counts: Counter[tuple[str, ...]] = Counter()
    for sentence in corpus:
        mapped = [token if token in vocabulary else UNK for token in sentence]
        padded = [BOS] * (n - 1) + mapped + [EOS]
        for index in range(n - 1, len(padded)):
            gram = tuple(padded[index - n + 1 : index + 1])
            context = gram[:-1]
            ngram_counts[gram] += 1
            context_counts[context] += 1
    return ngram_counts, context_counts


class NGramLanguageModel:
    """A count-based unigram, bigram, or trigram language model."""

    def __init__(
        self,
        n: int,
        vocabulary: set[str] | None = None,
        min_count: int = 2,
        max_vocab_size: int | None = 50_000,
    ) -> None:
        if n not in {1, 2, 3}:
            raise ValueError("This lab implementation supports n in {1, 2, 3}")
        self.n = n
        self.vocabulary = set(vocabulary) if vocabulary is not None else None
        self.min_count = min_count
        self.max_vocab_size = max_vocab_size
        self.ngram_counts: Counter[tuple[str, ...]] = Counter()
        self.context_counts: Counter[tuple[str, ...]] = Counter()

    def fit(self, corpus: Sequence[Sequence[str]]) -> "NGramLanguageModel":
        """Estimate count tables from tokenized training sentences."""
        if self.vocabulary is None:
            self.vocabulary = build_vocabulary(
                corpus,
                min_count=self.min_count,
                max_size=self.max_vocab_size,
            )
        self.ngram_counts, self.context_counts = count_ngrams(
            corpus, self.n, self.vocabulary
        )
        return self

    @property
    def vocabulary_size(self) -> int:
        self._require_fitted()
        return len(self.vocabulary)

    def _require_fitted(self) -> None:
        if self.vocabulary is None or not self.context_counts:
            raise RuntimeError("Call fit() before using the model")

    def _map_word(self, word: str) -> str:
        self._require_fitted()
        if word == BOS:
            return BOS
        return word if word in self.vocabulary else UNK

    def _history(self, context: Sequence[str] | None) -> tuple[str, ...]:
        if self.n == 1:
            return ()
        mapped = [self._map_word(word) for word in (context or [])]
        needed = self.n - 1
        return tuple(([BOS] * max(0, needed - len(mapped)) + mapped)[-needed:])

    def probability(
        self,
        context: Sequence[str] | None,
        word: str,
        smoothing: str = "mle",
    ) -> float:
        """Return P(word | context) using MLE or add-one smoothing."""
        self._require_fitted()
        if smoothing not in {"mle", "laplace"}:
            raise ValueError("smoothing must be 'mle' or 'laplace'")

        history = self._history(context)
        mapped_word = self._map_word(word)
        numerator = self.ngram_counts[history + (mapped_word,)]
        denominator = self.context_counts[history]
        if smoothing == "laplace":
            return (numerator + 1) / (denominator + self.vocabulary_size)
        return numerator / denominator if denominator else 0.0

    def _event_probability(
        self,
        history: tuple[str, ...],
        mapped_word: str,
        smoothing: str,
    ) -> float:
        """Fast probability path for already-normalized internal events."""
        numerator = self.ngram_counts[history + (mapped_word,)]
        denominator = self.context_counts[history]
        if smoothing == "laplace":
            return (numerator + 1) / (denominator + len(self.vocabulary))
        return numerator / denominator if denominator else 0.0

    def _sentence_events(
        self, sentence: Sequence[str]
    ) -> Iterator[tuple[tuple[str, ...], str]]:
        mapped = [self._map_word(word) for word in sentence]
        padded = [BOS] * (self.n - 1) + mapped + [EOS]
        for index in range(self.n - 1, len(padded)):
            yield tuple(padded[index - self.n + 1 : index]), padded[index]

    def sentence_log_probability(
        self, sentence: Sequence[str], smoothing: str = "mle"
    ) -> float:
        """Return the natural-log probability of a sentence, including </s>."""
        if smoothing not in {"mle", "laplace"}:
            raise ValueError("smoothing must be 'mle' or 'laplace'")
        log_probability = 0.0
        for context, word in self._sentence_events(sentence):
            probability = self._event_probability(context, word, smoothing)
            if probability == 0.0:
                return -math.inf
            log_probability += math.log(probability)
        return log_probability

    def sentence_probability(
        self, sentence: Sequence[str], smoothing: str = "mle"
    ) -> float:
        """Return sentence probability; long sequences may underflow to zero."""
        log_probability = self.sentence_log_probability(sentence, smoothing)
        return 0.0 if log_probability == -math.inf else math.exp(log_probability)

    def corpus_perplexity(
        self, corpus: Iterable[Sequence[str]], smoothing: str = "mle"
    ) -> float:
        """Compute token-level perplexity, counting one </s> event per sentence."""
        if smoothing not in {"mle", "laplace"}:
            raise ValueError("smoothing must be 'mle' or 'laplace'")
        total_log_probability = 0.0
        event_count = 0
        for sentence in corpus:
            for context, word in self._sentence_events(sentence):
                probability = self._event_probability(context, word, smoothing)
                if probability == 0.0:
                    return math.inf
                total_log_probability += math.log(probability)
                event_count += 1
        if event_count == 0:
            raise ValueError("Cannot compute perplexity for an empty corpus")
        return math.exp(-total_log_probability / event_count)

    def continuation_log_probability(
        self,
        context: Sequence[str],
        continuation: Sequence[str],
        smoothing: str = "laplace",
    ) -> tuple[float, int]:
        """Score only continuation tokens given an external context.

        The end-of-sentence token is deliberately excluded so candidate strings
        are scored exactly as provided. The returned count supports length
        normalization when candidates have different lengths.
        """
        history_words = list(context)
        total = 0.0
        for word in continuation:
            probability = self.probability(history_words, word, smoothing=smoothing)
            if probability == 0.0:
                return -math.inf, len(continuation)
            total += math.log(probability)
            history_words.append(word)
        return total, len(continuation)

    def next_word_distribution(
        self,
        context: Sequence[str],
        smoothing: str = "laplace",
        top_k: int = 10,
    ) -> list[tuple[str, float]]:
        """Return the highest-probability observed continuations.

        With Laplace smoothing, unseen words have equal non-zero mass but cannot
        outrank a word observed in the same context. Special tokens are omitted
        from human-facing predictions.
        """
        if top_k < 1:
            return []
        history = self._history(context)
        candidates = [
            (gram[-1], count)
            for gram, count in self.ngram_counts.items()
            if gram[:-1] == history and gram[-1] not in {BOS, EOS, UNK}
        ]
        candidates.sort(key=lambda item: (-item[1], item[0]))
        return [
            (word, self.probability(history, word, smoothing=smoothing))
            for word, _ in candidates[:top_k]
        ]


def train_unigram(
    corpus: Sequence[Sequence[str]], vocabulary: set[str] | None = None
) -> NGramLanguageModel:
    return NGramLanguageModel(1, vocabulary=vocabulary).fit(corpus)


def train_bigram(
    corpus: Sequence[Sequence[str]], vocabulary: set[str] | None = None
) -> NGramLanguageModel:
    return NGramLanguageModel(2, vocabulary=vocabulary).fit(corpus)


def train_trigram(
    corpus: Sequence[Sequence[str]], vocabulary: set[str] | None = None
) -> NGramLanguageModel:
    return NGramLanguageModel(3, vocabulary=vocabulary).fit(corpus)

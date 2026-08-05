from collections import Counter
import math
from typing import Sequence
from ..Tokenize import PuncTokenize, WordTokenize


def AvgWordLength(tokens: Sequence[str]) -> float:
    """Returns the average word length in characters."""
    if not tokens:
        return 0.0
    return sum(len(token) for token in tokens) / len(tokens)


def AvgSentenceLength(tokens: Sequence[str]) -> float:
    """Returns the average sentence length in words; requires sentence tokens."""
    if not tokens:
        return 0.0
    return sum(len(WordTokenize(sentence)) for sentence in tokens) / len(tokens)


def CharEntropy(tokens: Sequence[str]) -> float:
    """Returns the character entropy for the provided token sequence."""
    joined_tokens = "".join(tokens)
    if not joined_tokens:
        return 0.0

    characters = list(joined_tokens)
    counter_dict = Counter(characters)
    num_tokens = len(characters)
    probabilities = [count / num_tokens for count in counter_dict.values()]
    return -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)


def PuncEntropy(tokens: Sequence[str]) -> float:
    """Returns the punctuation entropy for the provided token sequence."""
    new_tokens = PuncTokenize("".join(tokens))
    if not new_tokens:
        return 0.0

    counter_dict = Counter(new_tokens)
    num_tokens = len(new_tokens)
    probabilities = [count / num_tokens for count in counter_dict.values()]
    return -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)


def UpperCaseFreq(tokens: Sequence[str]) -> float:
    """Frequency of upper case letters at the start of tokens."""
    if not tokens:
        return 0.0

    uppercase_total = sum(1 for token in tokens if token and token[0].isupper())
    return uppercase_total / len(tokens)

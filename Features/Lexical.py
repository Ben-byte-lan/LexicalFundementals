from collections import Counter
import math
import random
from typing import Sequence
from .Tools import FetchHapaxLegomma

"""Contains Lexical Metrics"""

def TTR(tokens: Sequence[str]) -> float:
    """Return the type-token ratio for a token sequence.
    """
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def MATTR(tokens: Sequence[str], window: int) -> float:
    """Return the moving-average type-token ratio.
    """
    if not tokens or window <= 0:
        return 0.0

    window = min(window, len(tokens))
    iterations = len(tokens) - window + 1
    if iterations <= 0:
        return 0.0

    return sum(TTR(tokens[i : i + window]) for i in range(iterations)) / iterations


def MSTTR(tokens: Sequence[str], segments: int) -> float:
    """Return the mean segmental TTR across evenly sized segments.
    """
    if not tokens or segments <= 0:
        return 0.0

    segments = min(segments, len(tokens))
    segment_length = len(tokens) // segments
    if segment_length == 0:
        return TTR(tokens)

    scores = []
    for index in range(segments):
        start = index * segment_length
        end = start + segment_length
        if index == segments - 1:
            end = len(tokens)
        if end > start:
            scores.append(TTR(tokens[start:end]))

    return sum(scores) / len(scores)


def WMSTTR(tokens: Sequence[str], words: int) -> float:
    """Return the mean TTR over consecutive word-based segments.
    """
    if not tokens or words <= 0:
        return 0.0

    segments = [tokens[i : i + words] for i in range(0, len(tokens), words)]
    return sum(TTR(segment) for segment in segments) / len(segments)


def Shannon_Entropy(tokens: Sequence[str]) -> float:
    """Return Shannon entropy for the provided token sequence.
    """
    if not tokens:
        return 0.0

    counter_dict = Counter(tokens)
    num_tokens = len(tokens)
    probabilities = [value / num_tokens for value in counter_dict.values()]
    return -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)


def Renyi_Entropy(tokens: Sequence[str], alpha: float) -> float:
    """Return Rényi entropy for the provided token sequence.
    """
    if not tokens:
        return 0.0

    if alpha == 1:
        return Shannon_Entropy(tokens)

    counter_dict = Counter(tokens)
    num_tokens = len(tokens)
    summation = sum((value / num_tokens) ** alpha for value in counter_dict.values())
    return (1 / (1 - alpha)) * math.log2(summation)


def Subsample_Entropy(tokens: Sequence[str], words: int, alpha: float = 1.0, epochs: int = 10) -> float:
    """Estimate entropy by averaging Rényi entropy across random subsamples
    """
    if not tokens or words <= 0 or epochs <= 0:
        return 0.0

    sample_size = min(words, len(tokens))
    summation = sum(Renyi_Entropy(random.sample(list(tokens), sample_size), alpha) for _ in range(epochs))
    return summation / epochs


def Yules_K(tokens: Sequence[str]) -> float:
    """Return Yule's K, a measure of lexical concentration.
    """
    if not tokens:
        return 0.0

    number = len(tokens)
    if number <= 1:
        return 0.0

    counts = Counter(tokens)
    frequencies = Counter(counts.values())
    summation = sum(freq * (frequency**2) for frequency, freq in frequencies.items())
    return 10000 * ((summation / (number**2)) - (1 / number))


def Yules_I(tokens: Sequence[str]) -> float:
    """Return the inverse of Yule's K for convenience."""
    if not tokens:
        return 0.0
    else:
        return 1 / Yules_K(tokens)


def Hapax(tokens:Sequence[str]) -> float:
    """Compute the frequency of Hapax Legomma."""
    return len(FetchHapaxLegomma(tokens))/len(tokens)

def HonoresH(tokens:Sequence[str])-> float:
    """A statistical metric of hapax legomma"""
    v = set(tokens)
    v1 = len(FetchHapaxLegomma(tokens))
    if v1==v:
        return 0.0
    else:
        return 100*math.log10(len(tokens))/(1-(len(v1)/(len(v))))

def SichelsS(tokens:Sequence[str]) -> float:
    """A statistical metric of hapex dilegomma"""
    return len(FetchHapaxLegomma(tokens,2))/len(set(tokens))
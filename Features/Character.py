from collections import Counter
import math
import random
from typing import Sequence
from Tokenize import WordTokenize, PuncTokenize
def AvgWordLength(tokens:Sequence[str]) -> float:
    """Returns the length of the average words characters"""
    if not tokens:
        return 0.0
    return sum([len(i) for i in tokens])/len(tokens)

def AvgSentenceLength(tokens:Sequence[str])->float:
    """Returns the length of the average sentence in terms of words requires sentence tokens"""
    if not tokens:
        return 0.0
    return sum([len(WordTokenize(i)) for i in tokens])/len(tokens)

def CharEntropy(tokens:Sequence[str])->float:
    """Entropy of a particular character"""
    new_tokens = list("".join(tokens))
    if not new_tokens:
        return 0.0
    counter_dict= Counter(new_tokens)
    num_tokens = len(new_tokens)
    probabilities = [value / num_tokens for value in counter_dict.values()]
    return -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)

def PuncEntropy(tokens: Sequence[str])->float:
    """Entropy of punctuations"""
    new_tokens = PuncTokenize("".join(tokens))
    if not new_tokens:
        return 0.0
    counter_dict= Counter(new_tokens)
    num_tokens = len(new_tokens)
    probabilities = [value / num_tokens for value in counter_dict.values()]
    return -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)
    
def UpperCaseFreq(tokens: Sequence[str])->float:
    """Frequency of upper case letters"""
    if not tokens:
        return 0.0
    total = [i for i in tokens if i and i[0].isupper()]
    return len(total)/len(tokens)


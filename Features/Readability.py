from .Character import AvgSentenceLength, SyllableFreq
from typing import Sequence, List
from collections import Counter
from statistics import stdev
from math import sqrt
from ..Tokenize import SentenceTokenize

def Flesch(tokens:Sequence[str])->float:
    return 206.835 - (1.015 * AvgSentenceLength(tokens)) - (84.6 * SyllableFreq(tokens))

def GonningHog(tokens:Sequence[str])->float:
    return  0.4 * (AvgSentenceLength(tokens) + SyllableFreq(tokens, t=True))

def ARI(tokens:Sequence[str])->float:
    if not tokens:
        return 0.0
    chars = len("".join(tokens))
    words = len(tokens)
    sentences = len(SentenceTokenize(" ".join(tokens)))
    return 4.71 * (chars/words) + .5 * (words/sentences) -21.43
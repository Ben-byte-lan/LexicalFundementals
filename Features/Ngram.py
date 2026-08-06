from .Tools import FetchNgrams
from collections import Counter
from typing import Sequence
from .Lexical import Shannon_Entropy, TTR




def NgramFreq(tokens: Sequence[str], n:int)->dict:
    Ngrams =FetchNgrams(tokens, n)
    NgramsC = Counter(FetchNgrams(tokens, n))
    return dict(map(lambda item: (item[0], item[1]/len(Ngrams)), NgramsC.items()))

def TopNgrams(tokens:Sequence[str], n:int,k:int)->list:
    return Counter(FetchNgrams(tokens, n)).most_common(k)

def NgramEntropy(tokens:Sequence[str], n:int)->float:
    return Shannon_Entropy(FetchNgrams(tokens,n))

def NgramTTR(tokens:Sequence[str], n:int)->float:
    return TTR(FetchNgrams(tokens,n))
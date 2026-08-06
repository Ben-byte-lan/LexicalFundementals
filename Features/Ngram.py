from .Tools import FetchNgrams
from collections import Counter
from typing import Sequence
from .Lexical import Shannon_Entropy, TTR




def NgramFreq(tokens: Sequence[str], n:int, char = False)->dict:
    Ngrams =FetchNgrams(tokens, n, characters=char)
    NgramsC = Counter(Ngrams)
    return dict(map(lambda item: (item[0], item[1]/len(Ngrams)), NgramsC.items()))

def TopNgrams(tokens:Sequence[str], n:int,k:int, char = False)->list:
    return Counter(FetchNgrams(tokens, n,characters=char)).most_common(k)

def NgramEntropy(tokens:Sequence[str], n:int,  char = False)->float:
    return Shannon_Entropy(FetchNgrams(tokens,n,characters=char))

def NgramTTR(tokens:Sequence[str], n:int,  char = False)->float:
    return TTR(FetchNgrams(tokens,n,characters=char))
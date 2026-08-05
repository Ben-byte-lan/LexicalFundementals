from typing import Sequence
from collections import Counter
def FetchNgrams(tokens:Sequence[str],characters: bool = False, n = 3):
    """"""
    new_list = []
    if characters:
        totals = list("".join(tokens))
        for i in range(len(totals)-n+1):
            new_list.append(tuple(totals[i:i+n]))

    else:
        for i in range(len(tokens)-n+1):
            new_list.append(tuple(tokens[i:i+n]))
    return new_list
        
            
def FetchHapaxLegomma(tokens:Sequence[str], n=1):
    objs = Counter(tokens)
    new_list = []
    for key, value in objs.items():
        if value == n:
            new_list.append(key)
    return new_list
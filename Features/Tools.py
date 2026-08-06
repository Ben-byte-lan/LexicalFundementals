from typing import Sequence, List
from collections import Counter
from statistics import stdev
import math
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

    
def BurrowsDelta(text1:Sequence[str], Corpus2:List[Sequence[str]],k)->float:
    """1 is test, 2 is main"""
    n_test = len(text1)
    n_docs = len(Corpus2)
    test_counts = Counter(text1)
    corpus_counts_per_doc = [Counter(doc) for doc in Corpus2]
    all_corpus_words = Counter([word for doc in Corpus2 for word in doc])
    top_k_words = [word for word, _ in all_corpus_words.most_common(k)]
    delta_sum = 0.0
    for word in top_k_words:
        f_test = test_counts[word] / n_test if n_test > 0 else 0
        doc_freqs = []
        for i, doc in enumerate(Corpus2):
            doc_len = len(doc)
            freq = corpus_counts_per_doc[i][word] / doc_len if doc_len > 0 else 0
            doc_freqs.append(freq)
        mu = sum(doc_freqs) / n_docs if n_docs > 0 else 0
        variance = sum((f - mu) ** 2 for f in doc_freqs) / n_docs
        sigma = math.sqrt(variance)
        if sigma == 0:
            sigma = 1e-10
        
        f_ref_total = all_corpus_words[word] / sum(len(doc) for doc in Corpus2)

        z_test = (f_test - mu) / sigma
        z_ref = (f_ref_total - mu) / sigma
        
        delta_sum += abs(z_test - z_ref)
    return delta_sum / k
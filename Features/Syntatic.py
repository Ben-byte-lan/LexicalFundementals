from Tokenize import PosTokenize
from typing import Sequence
from collections import Counter
import spacy
from statistics import median, mean, stdev

try:
    nlp = spacy.load("en_core_web_sm", disable=["ner"])
except OSError:
    nlp = spacy.blank("en")
    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")

def PosFreq(Tokens:Sequence[str])->dict:
    Postokens=PosTokenize(" ".join(Tokens))
    freqs = Counter((i[1] for i in Postokens))
    for k,v in freqs.items():
        freqs[k]=v/len(Postokens)
    return freqs

from typing import Sequence

BE_VERBS = {"be", "am", "is", "are", "was", "were", "been", "being"}

def PassiveFreq(SentenceTokens: Sequence[str]) -> float:

    if not SentenceTokens:
        return 0.0
    sublist = [PosTokenize(sentence, tag=None) for sentence in SentenceTokens]
    passive_count = 0

    for sentence in sublist:
        is_passive = False
        for w in range(len(sentence)):
            if sentence[w][0].lower() in BE_VERBS:
                if any(x[1] == "VBN" for x in sentence[w + 1:]):
                    is_passive = True
                    break
        
        if is_passive:
            passive_count += 1
    return passive_count / len(sublist)


class Syntactic:
    def __init__(self, sentence_tokens: Sequence[str]):
        self.sentence_tokens = sentence_tokens
        self.depths = []
        self.dependencies = Counter()
        self.dependencies_count = 0

        for doc in nlp.pipe(self.sentence_tokens):
            for sentence in doc.sents:
                root = sentence.root
                if root is None:
                    continue
                self.depths.append(self.get_tree_depth(root))

                for token in sentence:
                    if token.dep_ == "ROOT" or not token.dep_:
                        continue
                    self.dependencies[token.dep_] += 1
                    self.dependencies_count += 1

        if self.dependencies_count:
            self.dependencies = {
                relation: count / self.dependencies_count
                for relation, count in self.dependencies.items()
            }
        else:
            self.dependencies = {}

    def get_tree_depth(self, token) -> int:
        children = list(token.children)
        if not children:
            return 1
        return 1 + max(self.get_tree_depth(child) for child in children)

    def mean_tree_depth(self) -> float:
        return mean(self.depths) if self.depths else 0.0

    def median_tree_depth(self) -> float:
        return median(self.depths) if self.depths else 0.0

    def mode_tree_depth(self) -> float:
        if not self.depths:
            return 0.0
        return Counter(self.depths).most_common(1)[0][0]

    def stdv_tree_depth(self) -> float:
        if len(self.depths) < 2:
            return 0.0
        return stdev(self.depths)
    def dependency_relations(self) -> dict:
        return self.dependencies
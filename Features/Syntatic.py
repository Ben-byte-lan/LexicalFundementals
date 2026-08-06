from ..Tokenize import PosTokenize
from .Lexical import Shannon_Entropy
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
def PosEntropy(Tokens:Sequence[str])->float:
    Postokens=PosTokenize(" ".join(Tokens))
    return Shannon_Entropy(pos[1] for pos in Postokens)

class Syntactic:
    def __init__(self, sentence_tokens: Sequence[str]):
        self.sentence_tokens = sentence_tokens
        self.depths = []
        self.passivity= True
        self.dependencies = Counter()
        self.dependencies_count = 0
        self.passive = 0
        for doc in nlp.pipe(self.sentence_tokens):
            for sentence in doc.sents:
                root = sentence.root
                if root is None:
                    continue
                self.depths.append(self.get_tree_depth(root))

                for token in sentence:
                    if token.dep_ == "ROOT" or not token.dep_:
                        continue
                    if token.dep_ in {"auxpass", "nsubjpass"} and not self.passivity:
                        self.passive += 1
                        self.passivity = True
                    
                    self.dependencies[token.dep_] += 1
                    self.dependencies_count += 1

                self.passivity= False

        self.passive = self.passive/len(sentence_tokens)

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
    def PassiveVoiceFrequency(self)->float:
        return self.passive
    
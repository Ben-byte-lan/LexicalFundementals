from .Features import Character, Lexical, Ngram, Readability, Syntatic, Tools
import Tokenize 
from typing import Sequence,List
class Features:
    def __init__(self,text:str, n=3,k=15,segment=100, alpha=.5, words = 50):
        self.words = Tokenize.WordTokenize(text)
        self.sentences = Tokenize.SentenceTokenize(text)
        
        self.SyntaticClass = Syntatic.Syntactic(self.sentences)
        self.dataextract={
            "AvgWordLength": Character.AvgWordLength(self.self.words),
            "AvgSentenceLength": Character.AvgSentenceLength(self.words),
            "CharEntropy": Character.CharEntropy(self.words),
            "PuncEntropy":Character.PuncEntropy(self.words),
            "UpperCaseFreq": Character.UpperCaseFreq(self.words),
            "SyllablesFreq":Character.SyllableFreq(self.words),

            "TTR":Lexical.TTR(self.words),
            "MSTTR":Lexical.MSTTR(self.words,segment),
            "MATTR":Lexical.MATTR(self.words,segment),
            "HonoresH":Lexical.HonoresH(self.words),
            "RenyiEntropy":Lexical.Renyi_Entropy(self.words,alpha),
            "ShannonsEntropy":Lexical.Shannon_Entropy(self.words),
            "SichelsS":Lexical.SichelsS(self.words),
            "StopWordFreq":Lexical.StopWordFreq(self.words),
            "SubSampleEntropy":Lexical.Subsample_Entropy(self.words),
            "WMSTTR":Lexical.WMSTTR(self.words,words),
            "YulesK":Lexical.Yules_K(self.words),
            "YulesI":Lexical.Yules_I(self.words),
            "HapaxFreq":Lexical.Hapax(self.words),

            "NgramFreq":Ngram.NgramFreq(self.words,n),
            "NgramTTR":Ngram.NgramTTR(self.words,n),
            "NgramEntropy":Ngram.NgramEntropy(self.words,n),
            "TopNgrams":Ngram.TopNgrams(self.words,n,15),
            "CNgramFreq":Ngram.NgramFreq(self.words,n,char=True),
            "CNgramTTR":Ngram.NgramTTR(self.words,n,char=True),
            "CNgramEntropy":Ngram.NgramEntropy(self.words,n,char=True),
            "CTopNgrams":Ngram.TopNgrams(self.words,n,k,char=True),

            "Flesch":Readability.Flesch(self.words),
            "GonningHog":Readability.GonningHog(self.words),
            "ARI":Readability.ARI(self.words),

            "PosEntropy":Syntatic.PosEntropy(self.words),
            "PosFreq":Syntatic.PosFreq(self.words),
            "Dependencies":self.SyntaticClass.dependency_relations(),
            "MeanTreeDepth":self.SyntaticClass.mean_tree_depth(),
            "MedianTreeDepth":self.SyntaticClass.median_tree_depth(),
            "PassiveVoiceFreq":self.SyntaticClass.PassiveVoiceFrequency(),
            "ModeTreeDepth":self.SyntaticClass.mode_tree_depth(),
            "StdvTreeDepth":self.SyntaticClass.stdv_tree_depth()
        }
    def CompressDictionaries(self):
         """This process cannot be undone compresses all dicts into floats"""
         list_of_dicts = self.GetDicts(self)
         for tuples in list_of_dicts:
            prefix = tuples[0]
            for k,v in tuples[1].items():
                self.dataextract[f"{prefix}{k}"]=v
            if prefix in self.dataextract:
                self.dataextract.pop(prefix)
                   

    def GetVector(self):
            vector = []
            for k,v in self.dataextract.items():
                if isinstance(v,float) or isinstance(v,int):
                    vector.append((k,v))
            return vector

    def GetChoose(self, array: Sequence[str]):
            vector = []
            for k in array:
                vector.append((k,self.dataextract[k]))
            return vector

    def GetDicts(self):
            vector = []
            for k,v in self.dataextract.items():
                if isinstance(v,dict):
                    vector.append((k,v))
            return vector

    def GetBurrows(self,corpus:List[Sequence[str]],k=100):
            return Tools.BurrowsDelta(self.words,corpus,k)






        












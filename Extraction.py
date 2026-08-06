from .Features import Character, Lexical, Ngram, Readability, Syntatic, Tools
import Tokenize 


def FeatureExtact(text:str, n=3,k=15)->dict:
    words = Tokenize.WordTokenize(text)
    sentences = Tokenize.WordTokenize(text)

    SyntaticClass = Syntatic.Syntactic(sentences)



    dataextract={
        "AvgWordLength": Character.AvgWordLength(words),
        "AvgSentenceLength": Character.AvgSentenceLength(words),
        "CharEntropy": Character.CharEntropy(words),
        "PuncEntropy":Character.PuncEntropy(words),
        "UpperCaseFreq": Character.UpperCaseFreq(words),
        "SyllablesFreq":Character.SyllableFreq(words),

        "TTR":Lexical.TTR(words),
        "MSTTR":Lexical.MSTTR(words),
        "MATTR":Lexical.MATTR(words),
        "HonoresH":Lexical.HonoresH(words),
        "RenyiEntropy":Lexical.Renyi_Entropy(words),
        "ShannonsEntropy":Lexical.Shannon_Entropy(words),
        "SichelsS":Lexical.SichelsS(words),
        "StopWordFreq":Lexical.StopWordFreq(words),
        "SubSampleEntropy":Lexical.Subsample_Entropy(words),
        "WMSTTR":Lexical.WMSTTR(words),
        "YulesK":Lexical.Yules_K(words),
        "YulesI":Lexical.Hapax(words),

        "NgramFreq":Ngram.NgramFreq(words,n),
        "NgramTTR":Ngram.NgramTTR(words,n),
        "NgramEntropy":Ngram.NgramEntropy(words,n),
        "TopNgrams":Ngram.TopNgrams(words,n,15),
        "CNgramFreq":Ngram.NgramFreq(words,n,char=True),
        "CNgramTTR":Ngram.NgramTTR(words,n,char=True),
        "CNgramEntropy":Ngram.NgramEntropy(words,n,char=True),
        "CTopNgrams":Ngram.TopNgrams(words,n,k,char=True),

        "Flesch":Readability.Flesch(words),
        "GonningHog":Readability.GonningHog(words),
        "ARI":Readability.ARI(words),

        "PosEntropy":Syntatic.PosEntropy(words),
        "PosFreq":Syntatic.PosFreq(words),
        "Dependencies":SyntaticClass.dependency_relations(),
        "MeanTreeDepth":SyntaticClass.mean_tree_depth(),
        "MedianTreeDepth":SyntaticClass.median_tree_depth(),
        "PassiveVoiceFreq":SyntaticClass.PassiveVoiceFrequency(),
        "ModeTreeDepth":SyntaticClass.mode_tree_depth(),
        "StdvTreeDepth":SyntaticClass.stdv_tree_depth()
        

    }




        























    }

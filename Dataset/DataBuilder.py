from Dataset import Dataset
from dataclasses import asdict
import json
import os
from Tokenize import WordTokenize
from pathlib import Path
from FeatureExtractor import Features



def build():
    dataset= Dataset()
    main_folder = "..Test"
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith(".txt") and file.startswith("C"):
                file_path = os.path.join(root, file)
                push(file_path,dataset)
    print("DONE")
    dataset.save()
    

def chunk(filepath, n=1000):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    words= WordTokenize(content)
    segments = [
    words[i : i + n] for i in range(0, len(words), n)
    ]
    return segments

def featureselction(Feature:Features,method = "bing"):
    """DEFINITELY ADD THIS... make it so you can easily try out tons of different feature selection...
    
    8888888888888888888888888
    
    """


def push(filepath, dataset:Dataset):
    ps=Path(filepath)
    author = ps.parent.name
    book= ps.stem
    segments = chunk(filepath)
    for id in range(len(segments)):
        features = Features(text=" ".join(segments[id]))
        dataset.add_samples(features.GetVector,author,book,id)
        """create a feature selection function"""

        
def load():


    

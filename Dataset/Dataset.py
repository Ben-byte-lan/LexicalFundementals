from Sample import Sample
import json
from dataclasses import asdict
class Dataset:

    def __init__(self):
        self.samples = []

    def add_sample(self,features: dict,author: str,book: str,chunk_id: int):
        sample = Sample(
            features=features,
            author=author,
            book=book,
            chunk_id=chunk_id
        )

        self.samples.append(sample)
    def add(self, sample:Sample):
        self.samples.append(sample)

    def save(self):
    

        with open(f".Test\dataset.json", "w", encoding="utf-8") as file:
            json.dump(
                [asdict(sample) for sample in self.samples],
                file,
                indent=4
            )
    def load(self,file):
        with open(file, "r", encoding="utf-8") as file:
            self.samples=json.load(file,)
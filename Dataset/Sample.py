from dataclasses import dataclass

@dataclass
class Sample:
    features: dict
    author: str
    book: str
    chunk_id: int
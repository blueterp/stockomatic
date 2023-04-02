from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    sector: str
    industry: str
    price: float
    currency: str

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)
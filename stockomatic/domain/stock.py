from dataclasses import dataclass, asdict


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

    def to_dict(self):
        return asdict(self)

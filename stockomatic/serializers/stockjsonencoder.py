import json


class StockJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            return o.to_dict()
        except TypeError:
            return super().dumps(o)

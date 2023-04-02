import pytest
import json
from stockomatic.domain.stock import Stock
from stockomatic.serializers.stockjsonencoder import StockJsonEncoder


@pytest.fixture
def ibm_params():
    return {
        "ticker": "IBM",
        "sector": "Information Technology",
        "industry": "IT Consulting & Other Services",
        "price": 131.09,
        "currency": "USD",
    }


def test_stock_json_serializer(ibm_params):
    expected_string = """{
        "ticker": "IBM",
        "sector": "Information Technology",
        "industry": "IT Consulting & Other Services",
        "price": 131.09,
        "currency": "USD"
        }
    """
    ibm = Stock.from_dict(ibm_params)
    serialized = json.dumps(ibm, cls=StockJsonEncoder)
    assert json.loads(serialized) == json.loads(expected_string)


if __name__ == "__main__":
    pytest.main()

import pytest
from stockomatic.domain.stock import Stock
from stockomatic.use_cases.list_stocks import list_stocks
from unittest import mock


@pytest.fixture
def stock_params():
    return [
        {
            "ticker": "IBM",
            "sector": "Information Technology",
            "industry": "IT Consulting & Other Services",
            "price": 131.09,
            "currency": "USD",
        },
        {
            "ticker": "ACN",
            "sector": "Information Technology",
            "industry": "IT Consulting & Other Services",
            "price": 285.81,
            "currency": "USD",
        },
        {
            "ticker": "CTSH",
            "sector": "Information Technology",
            "industry": "IT Consulting & Other Services",
            "price": 60.93,
            "currency": "USD",
        },
        {
            "ticker": "IT",
            "sector": "Information Technology",
            "industry": "IT Consulting & Other Services",
            "price": 325.77,
            "currency": "USD",
        },
    ]


def test_list_stocks(stock_params):
    gt = [Stock.from_dict(s) for s in stock_params]
    repo = mock.Mock()
    repo.list.return_value = gt
    stocks = list_stocks(repo)

    assert gt == stocks


if __name__ == "__main__":
    pytest.main()

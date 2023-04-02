import pytest
from stockomatic.domain.stock import Stock

def test_stock_constructor():
    stock_params = {'ticker': 'IBM',
                    'sector': 'Information Technology',
                    'industry': 'IT Consulting & Other Services',
                    'price' : 131.09,
                    'currency': 'USD'
    }
    ibm = Stock(**stock_params)
    for key, value in stock_params.items():
        assert getattr(ibm, key) == value




if __name__ == "__main___":
    pytest.main()
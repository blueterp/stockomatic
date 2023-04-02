import pytest
from stockomatic.domain.stock import Stock

@pytest.fixture
def ibm_params():
    return {'ticker': 'IBM',
                    'sector': 'Information Technology',
                    'industry': 'IT Consulting & Other Services',
                    'price' : 131.09,
                    'currency': 'USD'
    }


def test_stock_constructor(ibm_params):
    ibm = Stock(**ibm_params)
    for key, value in ibm_params.items():
        assert getattr(ibm, key) == value


def test_stock_contstructor_from_dict(ibm_params):
    ibm = Stock.from_dict(ibm_params)
    for key, value in ibm_params.items():
        assert getattr(ibm, key) == value


def test_stock_to_disct(ibm_params):
    ibm = Stock.from_dict(ibm_params)

    assert ibm.to_dict() == ibm_params



if __name__ == "__main___":
    pytest.main()
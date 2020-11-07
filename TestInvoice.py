import pytest
import Invoice

@pytest.fixture()
def products():
    products = {'pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                    'notebook': {'qnt':5, 'unit_price': 7.5, 'discount': 10}}
    return products

def test_CanFind_InvoiceClass():
    invoice = Invoice()

def test_CanCalc():
    invoice = Invoice()
    invoice.totalImpure(products)
    assert invoice.totalImpure(products) == 75
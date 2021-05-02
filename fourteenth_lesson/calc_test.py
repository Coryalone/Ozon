import pytest
from testing_example import Calculator


@pytest.fixture()
def my_decorator_class():
    return Calculator()

def test_positive_sum_with_number(my_decorator_class):
    a = 6
    b = 5
    assert my_decorator_class.sum(a, b) == a + b

def test_neganive_sum_with_number(my_decorator_class):
    a = '6'
    b = 5
    with pytest.raises(TypeError):
        my_decorator_class.sum(a, b)

def test_missing_param_for_sum(my_decorator_class):
    a = 1
    with pytest.raises(TypeError):
        my_decorator_class.sum(a)

def test_positive_mult(my_decorator_class):
    a = 2
    b = 3
    assert my_decorator_class.mult(a, b) == a * b


def test_neganive_mult(my_decorator_class): #в Питоне можно умножать строки на число, по этому для негативнго тестрования выбрал сет.
    a = {'6'}
    b = 5
    with pytest.raises(TypeError):
        my_decorator_class.mult(a, b)

def test_missing_param_for_mulr(my_decorator_class):
    a = 1
    with pytest.raises(TypeError):
        my_decorator_class.mult(a)


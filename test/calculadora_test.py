import pytest
from calculadora import *

@pytest.mark.parametrize('operacion, valores, resultado', [
    ('SUMA', [10,20,40,50,60], 180),
    ('RESTA', [15,5], 10),
    ('RESTA', [15], 15),
])
def test_calculadora(operacion, valores, resultado):
    respuesta = calculadora(operacion, *valores)
    assert respuesta == resultado
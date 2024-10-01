# importando funções da pasta principal
from src.atp import adicionar, subtrair, multiplicar, dividir

# funções com operações

def test_adicionar(x, y):
    assert adicionar(5, 2) == 7

def test_subtrair(x, y):
    assert subtrair(8, 7) == 1

def test_multiplicar(x, y):
    assert multiplicar(3, 2) == 6

def test_dividir(x, y):
    assert dividir(6, 3) == 2
    assert dividir(1, 0) == "Erro! Divisão por zero."

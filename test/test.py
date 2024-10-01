# importando funções da pasta principal
from src.atp import adicionar, subtrair, multiplicar, dividir

# funções com operações

def test_adicionar():
    assert adicionar(5, 2) == 7

def test_subtrair():
    assert subtrair(8, 7) == 1

def test_multiplicar():
    assert multiplicar(3, 2) == 6

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(1, 0) == "Erro! Divisão por zero."

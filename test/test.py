# importando funções da pasta principal
from src.atp import *

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


# opções de inputs
print("Qual operação deseja realizar?")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# looping de funcionamento da calculadora
while True:
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

        # Pergunta ao usuário se deseja continuar ou sair
        proxima = input("Deseja fazer outra operação? (s/n): ")
        if proxima.lower() != 's':
            break
    else:
        print("Opção inválida, escolha 1 número de 1 a 4.")
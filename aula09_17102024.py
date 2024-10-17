#somar, multiplicar, subtrair, dividir
# Gera um número aleatório entre 1 e 100

#SOMAR

import random

def somar_numeros_aleatorios():
    a = random.randint(1, 100)  
    b = random.randint(1, 100)  
    resultado = a + b
    return f"A soma de {a} e {b} é: {resultado}"

#COMO USAR
print(somar_numeros_aleatorios())


#SUBTRAIR  
  
import random

def subtrair_numeros_aleatorios():
    a = random.randint(1, 100)  
    b = random.randint(1, 100)  
    resultado = a - b
    return f"A subtração de {a} menos {b} é: {resultado}"

#COMO USAR
print(subtrair_numeros_aleatorios())


#MULTIPLICAR

import random

def multiplicar_numeros_aleatorios():
    a = random.randint(1, 100)  
    b = random.randint(1, 100)  
    resultado = a * b
    return f"A multiplicação de {a} e {b} é: {resultado}"

#COMO USAR
print(multiplicar_numeros_aleatorios())


#DIVIDIR

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

#COMO USAR
num1 = 10
num2 = 2
print(dividir(num1, num2))  

num3 = 10
num4 = 0
print(dividir(num3, num4))  


import random
def gerando_numeros(quantidade,valor_minimo,valor_maximo):
    return[random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]



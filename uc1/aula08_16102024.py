# #FUNÇÕES:

def somar(parametro1,parametro2):
    return parametro1+parametro2
print(somar(20,30))
    
def subtrair(parametro1,parametro2):
    parametro1=int(input('Número 1:'))
    parametro2=int(input('Número 2:'))
    return parametro1-parametro2

print(subtrair())


#ATIVIDADE ASSISTIDA:

#Crie uma funçao para multiplicar dois números quaisquer:

def multiplicar():
    num1=float(input('Digite o primeiro número:'))
    num2=float(input('Digite o segundo número:'))
    return f'o resultado dos dois números dos dois números multiplicados é {num1*num2}'

print(multiplicar())

#-----------------------------------------------------------------------------------------------------

import random #trabalhar com dados gerados aleatoriamente

#criar uma função que me gere dois números aleatórios dentro de um intervalo

def doisnum_aleatorios(quantidade,numero_minimo,numero_maximo):
    for i in range(quantidade):
        return random.randint(numero_minimo,numero_maximo)
    
    numeros=doisnum_aleatorios(1,100)
    print(numeros)

    
    
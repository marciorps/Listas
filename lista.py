preco_1 = 10
preco_2 = 20
preco_3 = 30
# Listas
precos = [10, 20, 30, 40, 50, 60, 100, 250, 230, 560, 23, 74]
print(precos[0]) #Índice
print(precos[precos.index(100)])
# Listas no Python sõa dinâmicas(aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])
# Maneiras diferentes de gerar uma lista
# Multiplicação de valores(repetição)
listas_de_noves = [9] * 10
lista_de_testes = ['Teste'] * 10
print(listas_de_noves)
print(lista_de_testes)
# Usando gerador Range(Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
# Gerar apartir de strings
print(list('Bem-vindo as treinamento'))
# Lista de listas(matriz)
matriz_de_nomes = [['Carol', 30],['Marcos', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(  matriz_de_nomes[1][0])

#Desafio1
## Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante seu dia e imprima na tela
objetos_dia =['Carro', 'computador', 'Celuar']
print(objetos_dia)
# Desafio2
## Usando apenas uma linha de código, crie uma lista de 10 a 131
print(list(range(10, 132)))
#Desafio 3
## Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
lista_numeros = list(range(10, 132))
print(objetos_dia, lista_numeros)

#Desafio4
## Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos que você mais usa durante o dia, mas
#agora dentro de cada item vai colocar uma informação extra, coloque o valor em reais desses objeto também e imprima ele na tela
mais_usados = [['Carro', 'R$20.000,00'], ['computador', 'R$2.000,00'], ['celular', 'R$1.000,00']]
print(mais_usados[0][0])
print(mais_usados[1])
print(mais_usados[2])


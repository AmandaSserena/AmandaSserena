# %% exercicío 1
soma = 1 + 2

print("A soma de 1 e 2 é", soma)

# %% exercicío 2
subtração = 10 - 8

print("A subtração de 10 e 8 é", subtração)

# %% exercicío 3
multiplicação = 4 * 3

print("A multiplicação de 4 e 3 é", multiplicação)

# %% exercicío 4
print(25 / 32)

# %% exercicío 5
print(25 + 10)

# %% exercicío 6
potencia = 2 ** 10

print("A potência de  vale:", potencia)

# %% exercicío 7

notas = [7, 8, 6, 9]
soma = 0

for nota in notas:
    soma += nota

print("A  média aritmética", soma / len(notas))

# %% exercicio 8
base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))

print("A área do retângulo é:", altura)
# %% exercicio 10
comprimento_caixa = float(input("insira o comprimento(cm) da caixa: "))
largura_caixa = float(input("insira a largura(cm) da caixa: "))
altura_caixa = float(input("insira a altura(cm) da caixa: "))

volume_caixa = comprimento_caixa * largura_caixa * altura_caixa

print("O volume da caixa é:", volume_caixa)

# %% exercicio 11

def dar_desconto( valor: float, desconto: float):
    return valor - (valor * desconto)

desconto = float(input())

print(dar_desconto(100, desconto))

# %% exercicio 12

velocidade_carro = float(input("Digite a velocidade média do veículo (em km/h): "))
tempo_percurso = float(input("Digite o tempo de percurso (em horas): "))

distancia = velocidade_carro * tempo_percurso

print("A distância percorrida é de", distancia, "km.")

# %% exercicio 13
valor_inicial = float(input("digite o valor inicial; "))
taxa_juros = float(input("digite a taxa de juros: "))
tempo_aplicacao = float(input("digite o tempo de aplicação: "))

valor_final = valor_inicial * (1 + taxa_juros) ** tempo_aplicacao

print("O valor final da aplicação financeira é: ", valor_final)


# %% exercio 14

nota_1 = float(input("Digite a primeira nota: "))
peso_1 = int(input("Digite o peso da primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
peso_2 = int(input("Digite o peso da segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
peso_3 = int(input("Digite o peso da terceira nota: "))

soma_notas = nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3
soma_pesos = peso_1 + peso_2 + peso_3
media = soma_notas/soma_pesos

print("A média ponderada é: ", media)

# %%
notas: list[float] = []
pesos: list[int] = []

for i in range(0, 3):
    notas.append(float(input("Digite a {indice}˚ nota: ".format(indice = i))))
    pesos.append(float(input("Digite o {indice}˚ peso: ".format(indice = i))))
    
soma_notas: float = 0
soma_pesos: float = 0

for i in range(0, 3):
    soma_pesos += pesos[i]
    soma_notas += notas[i] * pesos[i]
    
media = soma_notas / soma_pesos

print("A média ponderada é: {media}".format(media = media))




# %%

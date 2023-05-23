import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
 
os.system('cls')

# VETORES DECLARADOS DAS TABELAS
coordenadax = []
coordenaday = []
forcax = []
forcay = []
reacaox = []
reacaoy = []
barra1 = []
barra2 = []
Ls = []
sens = []
coss = []


# INICIO DO PROGRAMA
print("                                                 Seja bem-vindo(a) ao nosso Programa de Cálculo Estrutural.")
print("           Para facilitar a execução do programa, imagine o sistema de treliças em forma de coordenadas cartesianas. Os eixos X e Y estão na escala de metros.")
print("                                                             As forças estão na escala de 'kN'")
print("                                                             Presione 'enter' para prosseguir!\n")
inicio=input("                                                                             ")
os.system('cls')



# ENTRADA DAS COORDENADAS DOS NÓS E FORÇAS APLICADAS EXTERNAS NA TRELIÇA
while True: # validação entrada de quantos nós
    entrada = input('Quantos nós a trelica terá?: ')
    if entrada.isdigit():
        n = int(entrada)
        break
    else:
        print("Entrada inválida. Tente novamente.")
print("\n")



for i in range(n):
   while True: # validação da entrada para coordenada x
        entrada = input('Insira a Coordenada X do Nó [{}]: '.format(i + 1))
        if entrada.isdigit():
            x = int(entrada)
            coordenadax.append(x)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   while True: # validação da entrada para coordenada y
        entrada = input('Insira a Coordenada Y do Nó [{}]: '.format(i + 1))
        if entrada.isdigit():
            y = int(entrada)
            coordenaday.append(y)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   while True:
        entrada = input('Insira a força aplicada em FX neste Nó [{}]: '.format(i + 1))
        if entrada.lstrip("-").isdigit():
            fx = int(entrada)
            forcax.append(fx)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   while True:
        entrada = input('Insira a força aplicada em FY neste Nó [{}]: '.format(i + 1))
        if entrada.lstrip("-").isdigit():
            fy = int(entrada)
            forcay.append(fy)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   while True:
        entrada = input('Insira a reação de apoio em X para o Nó [{}] (1 para rolete, 0 para nenhuma): '.format(i + 1))
        if entrada.isdigit():
            reacao_x = int(entrada)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   while True:
        entrada = input('Insira a reação de apoio em Y para o Nó [{}] (1 para rolete, 0 para nenhuma): '.format(i + 1))
        if entrada.isdigit():
            reacao_y = int(entrada)
            break
        else:
            print("Entrada inválida. Tente novamente.")

   reacaox.append(reacao_x)
   reacaoy.append(reacao_y)
   print("\n") 



# Após a leitura dos dados, adiciona-se à tabelanos e printa a mesma
tabelanos = pd.DataFrame({'X': coordenadax, 'Y': coordenaday, 'FX': forcax, 'FY': forcay, 'RX': reacaox, 'RY': reacaoy})
tabelanos.index += 1
print("\nInformações dos nós da treliça:")
print(tabelanos, "\n")



# ENTRADA DAS BARRAS DA TRELIÇA (QUAIS NÓS SE LIGAM ENTRE SI)
print('Quais nós estarão interligados entre si? ')
continuar = True
# simulando um do-while
while continuar:
    x1 = int(input('Insira o Primeiro Nó a ser ligado: '))
    barra1.append(x1)
    y1 = int(input('Insira o Segundo Nó a ser ligado: '))
    barra2.append(y1)

    resposta = input("Deseja continuar? (S/N): ")
    if resposta.lower() != "s":
        continuar = False

tabelabarras = pd.DataFrame({'N1': barra1, 'N2': barra2})
tabelabarras.index += 1

# CÁLCULO DAS FORÇAS DA TRELIÇA








# PLOTAGEM DO GRÁFICO QUE REPRESENTA A TRELIÇA
plt.figure(1, figsize=(12,4.5))
for barra in tabelabarras.index:
  N1, N2 = tabelabarras.loc[barra, ['N1', 'N2']]
  x2, y2 = tabelanos.loc[N1, ['X', 'Y']]
  x3, y3 = tabelanos.loc[N2, ['X', 'Y']]

  X = np.array([x2, x3])
  Y = np.array([y2, y3])
  plt.plot(X, Y, color='black')

# IMPORTANDO DADOS DOS NÓS NO GRÁFICO
for no in tabelanos.index:
    X, Y, FX, FY, RX, RY = tabelanos.loc[no]

    plt.scatter(X, Y, s=50, color='grey', marker="o")

    if RX == 1:
        plt.scatter(X,Y,400,marker =5,zorder = -2,color='blue')
    if RY == 1:
        plt.scatter(X,Y,400,marker =6,zorder = -2,color='blue')

    if FX > 0:
        plt.arrow(X - 1.5, Y, 1, 0, color='red', width=0.05)
        plt.text(X - 1.5, Y, '{:.2f}kN'.format(FX/1000), va='bottom')
    if FX < 0:
        plt.arrow(X + 1.5, Y, -1, 0, color='red', width=0.05)
        plt.text(X + 0.50, Y, '{:.2f}kN'.format(FX/1000), va='bottom')
    if FY > 0:
        plt.arrow(X, Y - 1.50, 0, 1, color='red', width=0.05)
        plt.text(X, Y + 0.50, '{:.2f}kN'.format(FY/1000), va='bottom', rotation=90)
    if FY < 0:
        plt.arrow(X, Y + 1.50, 0, -1, color='red', width=0.05)
        plt.text(X, Y + 0.50, '{:.2f}kN'.format(FY/1000), va='bottom', rotation=90)

for barra in tabelabarras.index:
   
   N1 = tabelabarras.loc[barra, 'N1']
   N2 = tabelabarras.loc[barra, 'N2']
   
   x1, y1 = tabelanos.loc[N1, ['X','Y']]
   x2, y2 = tabelanos.loc[N2, ['X','Y']]
   # O comprimento da barra é dado pelo teorema de Pitagoras
   Lx = x2 - x1
   Ly = y2 - y1    
   L = np.sqrt(Lx**2 + Ly**2)
   # Aplicando a lei do seno e cosseno:
   sen = Ly/L
   cos = Lx/L
   # Inserindo nas listas
   Ls.append(L)
   sens.append(sen)
   coss.append(cos)
   
# Inserindo as informações na tabela das barras
tabelabarras['L'] = Ls
tabelabarras['sen'] = sens
tabelabarras['cos'] = coss

print("\nInformações das barras da treliça:")
print(tabelabarras, "\n") 

# Após todo o pediodo de entrada de informações pelo usuário, exibe o grafico
plt.figure(1, figsize=(12, 4.5))               # Criando a figura e definindo seu número e tamanho em X e Y
plt.xlim(0,150) ; plt.ylim(-3,150)             # Definindo os limites de cada eixo
plt.grid(True)                              # Plotando a grade
plt.title('Cálculo Estrutural de Treliças')
plt.show()


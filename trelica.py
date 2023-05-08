import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#VETORES DECLARADOS DAS TABELAS
coordenadax = []
coordenaday = []
forcax = []
forcay = []
barra1 = []
barra2 = []

#ENTRADA DAS COORDENADAS DOS NÓS E FORÇAS APLICADAS EXTERNAS NA TRELIÇA
n = int(input('Quantos nos tera na trelica? :'))

for i in range(n):
  x = int(input('Insira a Coordenada X do No:'))
  coordenadax.append(x)
  y = int(input('Insira a Coordenada Y do No:'))
  coordenaday.append(y)
  fx = int(input('Insira a forca aplicada em FX neste no:'))
  forcax.append(fx)
  fy = int(input('Insira a forca aplicada em FY neste no:'))
  forcay.append(fy)

tabelanos = pd.DataFrame({'X': coordenadax, 'Y': coordenaday, 'FX': forcax, 'FY': forcay})
tabelanos.index += 1
print(tabelanos)

#ENTRADA DAS BARRAS DA TRELIÇA (QUAIS NÓS SE LIGAM ENTRE SI)
print('Quais nos estarao interligados entre si? ')
continuar = True
#simulando um do-while
while continuar:
    x1 = int(input('Insira o Primeiro No a ser ligado'))
    barra1.append(x1)
    y1 = int(input('Insira o Segundo No a ser ligado'))
    barra2.append(y1)

    resposta = input("Deseja continuar? (S/N) ")
    if resposta.lower() != "s":
        continuar = False

tabelabarras = pd.DataFrame({'N1': barra1, 'N2': barra2})
tabelabarras.index += 1
print(tabelabarras)

#CÁLCULO DAS FORÇAS DA TRELIÇA








#PLOTAGEM DO GRÁFICO QUE REPRESENTA A TRELIÇA
for barra in tabelabarras.index:
  N1, N2 = tabelabarras.loc[barra, ['N1', 'N2']]
  x2, y2 = tabelanos.loc[N1, ['X', 'Y']]
  x3, y3 = tabelanos.loc[N2, ['X', 'Y']]

  X = np.array([x2, x3])
  Y = np.array([y2, y3])
  print(X)
  print(Y)
  plt.plot(X, Y)

plt.show()

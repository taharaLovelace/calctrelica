import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

coordenadax = []
coordenaday = []
forcax = []
forcay = []

#entrada das coordenadas dos nós e forças da treliça
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

tabela = pd.DataFrame({'X': coordenadax, 'Y': coordenaday, 'FX': forcax, 'FY': forcay})
print(tabela)

#calculo das forças da treliça








#plotagem do gráfico que representa a treliça

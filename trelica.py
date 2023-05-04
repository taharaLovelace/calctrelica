import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

coluna = 'X Y RX RY FX FY '.split()
linha = '1 2 3 4 5 6 7 8 9'.split()
coordenax = []
coordenaday = []

n = int(input('Quantos nos tera na trelica? :'))

for i in range(n):
  x = int(input('Insira a Coordenada X do No:'))
  coordenax.append(x)
  y = int(input('Insira a Coordenada Y do No:'))
  coordenaday.append(y)

print(coordenax)
print(coordenaday)
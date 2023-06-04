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
Es = []
As = []

# INICIO DO PROGRAMA
print("                                                 Seja bem-vindo(a) ao nosso Programa de Cálculo Estrutural.")
print(
    "           Para facilitar a execução do programa, imagine o sistema de treliças em forma de coordenadas cartesianas. Os eixos X e Y estão na escala de metros.")
print("                                                             As forças estão na escala de 'kN'")
print("                                                             Presione 'enter' para prosseguir!\n")
inicio = input("                                                                             ")
os.system('cls')

while True:  # validação entrada de quantos nós
    entrada = input('Quantos nós a trelica terá?: ')
    if entrada.isdigit():
        if entrada == '0':
            print("Entrada inválida, fim do programa!!!!")
            os._exit(0)
        n = int(entrada)
        break
    else:
        print("Entrada inválida. Tente novamente.")
print("\n")


# ENTRADA DAS COORDENADAS DOS NÓS E FORÇAS APLICADAS EXTERNAS NA TRELIÇA
for i in range(n):
    while True:
        entrada = input('Insira a Coordenada X do Nó [{}]: '.format(i + 1))
        try:
            x = float(entrada)
            coordenadax.append(x)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    while True:
        entrada = input('Insira a Coordenada Y do Nó [{}]: '.format(i + 1))
        try:
            y = float(entrada)
            coordenaday.append(y)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    while True:
        entrada = input('Insira a força aplicada em FX neste Nó [{}]: '.format(i + 1))
        try:
            fx = float(entrada)
            forcax.append(fx)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    while True:
        entrada = input('Insira a força aplicada em FY neste Nó [{}]: '.format(i + 1))
        try:
            fy = float(entrada)
            forcay.append(fy)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    
    while True:
        entrada = input("Insira a reação de apoio para o Nó [{}]. Digite 'rolete' ou 'pino' ou 'nada': ".format(i + 1))
        if entrada == "rolete":
            reacao_x = 0
            reacao_y = 1
            break
        elif entrada == "pino":
            reacao_x = 1
            reacao_y = 1
            break
        elif entrada == "nada":
            reacao_x = 0
            reacao_y = 0
            break
        else:
            print("Opção inválida. Tente novamente.")

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
# simulando um do-while -> com critério de parada sendo algo diferente de 's'.
while continuar:
    x1 = int(input('Insira o Primeiro Nó a ser ligado: '))
    barra1.append(x1)
    y1 = int(input('Insira o Segundo Nó a ser ligado: '))
    barra2.append(y1)

    resposta = input("Deseja continuar? (S/N): ")
    if resposta.lower() != "s":
        continuar = False
    print("\n")

tabelabarras = pd.DataFrame({'N1': barra1, 'N2': barra2})
tabelabarras.index += 1

try:
    # PLOTAGEM DO GRÁFICO QUE REPRESENTA A TRELIÇA
    plt.figure(1, figsize=(12, 4.5))
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
            plt.scatter(X, Y, 400, marker=5, zorder=-2, color='blue')
        if RY == 1:
            plt.scatter(X, Y, 400, marker=6, zorder=-2, color='blue')

        if FX > 0:
            plt.arrow(X - 1.5, Y, 1, 0, color='red', width=0.05)
            plt.text(X - 1.5, Y, '{:.2f}kN'.format(FX / 1000), va='bottom')
        if FX < 0:
            plt.arrow(X + 1.5, Y, -1, 0, color='red', width=0.05)
            plt.text(X + 0.50, Y, '{:.2f}kN'.format(FX / 1000), va='bottom')
        if FY > 0:
            plt.arrow(X, Y - 1.50, 0, 1, color='red', width=0.05)
            plt.text(X, Y + 0.50, '{:.2f}kN'.format(FY / 1000), va='bottom', rotation=90)
        if FY < 0:
            plt.arrow(X, Y + 1.50, 0, -1, color='red', width=0.05)
            plt.text(X, Y + 0.50, '{:.2f}kN'.format(FY / 1000), va='bottom', rotation=90)

    for barra in tabelabarras.index:
        N1 = tabelabarras.loc[barra, 'N1']
        N2 = tabelabarras.loc[barra, 'N2']

        x1, y1 = tabelanos.loc[N1, ['X', 'Y']]
        x2, y2 = tabelanos.loc[N2, ['X', 'Y']]
        # O comprimento da barra é dado pelo teorema de Pitagoras
        Lx = x2 - x1
        Ly = y2 - y1
        L = np.sqrt(Lx ** 2 + Ly ** 2)
        # Aplicando a lei do seno e cosseno:
        sen = Ly / L
        cos = Lx / L
        # Inserindo nas listas
        Ls.append(L)
        sens.append(sen)
        coss.append(cos)
        As.append(0.01)             #CARACTERÍSTICAS DAS BARRAS A e E PARA A MONTAGEM DA MATRIZ DE RIGIDEZ
        Es.append(210000000000)     # módulo de elasticidade do aço estrutural


    # Inserindo as novas informações na tabela das barras
    tabelabarras['L'] = Ls
    tabelabarras['sen'] = sens
    tabelabarras['cos'] = coss
    tabelabarras['A'] = As
    tabelabarras['E'] = Es

    print("\nInformações das barras da treliça:")
    print(tabelabarras, "\n")

    # CÁLCULO DAS FORÇAS DA TRELIÇA

    maxgl = 2 * len(tabelanos.index)  # aloca previamente uma matriz de acordo com o numero de nós da treliça
    K = np.zeros([maxgl, maxgl])

    for barra in tabelabarras.index:
        N1, N2, L, sen, cos, A, E = tabelabarras.loc[barra]

        #Matriz de Rigidez Local
        Kl = E * A / L * np.array([[1, 0, -1, 0],
                                [0, 0, 0, 0],
                                [-1, 0, 1, 0],
                                [0, 0, 0, 0]])

        # Matriz de rotação
        Mrot = np.array([[cos, sen, 0, 0],
                        [-sen, cos, 0, 0],
                        [0, 0, cos, sen],
                        [0, 0, -sen, cos]])

        Klr = np.dot(np.dot(Mrot.T, Kl), Mrot)

        #Graus de liberdade
        gl1 = int(2 * N1 - 1)       #é necessário o int pois como os gls serão usados
        gl2 = int(2 * N1)           #para index, nao podem possuir ponto flutuante
        gl3 = int(2 * N2 - 1)
        gl4 = int(2 * N2)

        #Construção da Matriz Global de Rigidez
        K[gl1 - 1:gl2, gl1 - 1:gl2] += Klr[0:2, 0:2]
        K[gl3 - 1:gl4, gl1 - 1:gl2] += Klr[2:4, 0:2]
        K[gl1 - 1:gl2, gl3 - 1:gl4] += Klr[0:2, 2:4]
        K[gl3 - 1:gl4, gl3 - 1:gl4] += Klr[2:4, 2:4]
    #MATRIZ PARA O CÁLCULO DAS REAÇÕES DE APOIO
    K2 = K.copy()  # Alocando a matriz em outro espaço de memória
    for no in tabelanos.index:
        RX, RY = tabelanos.loc[no, ['RX', 'RY']]
        gl1 = int(2 * no - 1)
        gl2 = int(2 * no)

        if RX == 1:
            K2[:, gl1 - 1] = 0
            K2[gl1 - 1, :] = 0
            K2[gl1 - 1, gl1 - 1] = 1


        if RY == 1:
            K2[:, gl2 - 1] = 0
            K2[gl2 - 1, :] = 0
            K2[gl2 - 1, gl2 - 1] = 1

    #CONSTRUÇÃO DO VETOR DE FORÇAS
    F = np.zeros([maxgl])

    for no in tabelanos.index:
        FX, FY = tabelanos.loc[no, ['FX', 'FY']]
        gl1 = int(2 * no - 1)
        gl2 = int(2 * no)

        if FX != 0:
            F[gl1-1] = FX           #-1 para corrigir a posição do index
        if FY != 0:
            F[gl2-1] = FY
    D = np.linalg.solve(K2, F)
    R = np.dot(K, D)
    print(R)

    # PLOTAGEM DO GRÁFICO QUE REPRESENTA A TRELIÇA
    plt.figure(2, figsize=(12, 4.5))
    for barra in tabelabarras.index:
        N1, N2 = tabelabarras.loc[barra, ['N1', 'N2']]
        x2, y2 = tabelanos.loc[N1, ['X', 'Y']]
        x3, y3 = tabelanos.loc[N2, ['X', 'Y']]

        X = np.array([x2, x3])
        Y = np.array([y2, y3])
        plt.plot(X, Y, color='black')

    # IMPORTANDO DADOS DOS NÓS NO GRÁFICO
    for no in tabelanos.index:
        X, Y, RX, RY = tabelanos.loc[no, ['X','Y','RX','RY']]
        plt.scatter(X, Y, s=50, color='grey', marker="o")
        gl1 = int(2 * no - 1)
        gl2 = int(2 * no)

        if RX == 1:
            reacX = R[gl1-1]

            plt.arrow(X - 1.5, Y, 1, 0, color='red', width=0.05)
            plt.text(X - 1.5, Y, '{:.2f}kN'.format(reacX / 1000), va='bottom')
        if RY == 1:
            reacY =R[gl2-1]
            plt.arrow(X, Y - 1.50, 0, 1, color='red', width=0.05)
            plt.text(X, Y + 0.50, '{:.2f}kN'.format(reacY / 1000), va='bottom', rotation=90)

    # Determinação dos esforços nas barras
    Esf = []

    for barra in tabelabarras.index:
        N1, N2, L, sen, cos, A, E = tabelabarras.loc[barra]
        
        # Matriz de rigidez no sistema local 
        Kl = E*A/L*np.array([[ 1, 0,-1, 0],
                            [ 0, 0, 0, 0], 
                            [-1, 0, 1, 0],
                            [ 0, 0, 0, 0]])

        # Matriz de rotação
        Mrot = np.array([[ cos,  sen,    0,   0],
                        [-sen,  cos,    0,   0],
                        [    0,   0,  cos, sen],
                        [    0,   0, -sen, cos]])
        
        # Determinação dos gls
        gl1 = int(2*N1-1)
        gl2 = int(2*N1)
        gl3 = int(2*N2-1)
        gl4 = int(2*N2)
        
        # Capturar os deslocamentos
        Dlg = np.zeros([4])
        Dlg[0] = D[gl1-1]
        Dlg[1] = D[gl2-1]
        Dlg[2] = D[gl3-1]
        Dlg[3] = D[gl4-1]
        
        # Rotaciona Dlg
        Dl = np.dot(Mrot, Dlg)
        
        # Determina esforços no sentido da barra 
        Fl = np.dot(Kl, Dl)
        FAx = Fl[2]
        Esf.append(FAx)
    # Colocando Esf no dataframe de barras
    tabelabarras['Esf'] = Esf
    tabelabarras
    # Colocando deslocamentos nodais em Nós
    Dx = []
    Dy = []

    for no in tabelanos.index:
        gl1 = int(2*no-1)
        gl2 = int(2*no)
        
        Dx.append(D[gl1-1])
        Dy.append(D[gl2-1])

    tabelanos['Dx'] = Dx
    tabelanos['Dy'] = Dy 

    tabelanos

    # Plotando esforços nas barras
    plt.figure(3, figsize=(12,3))
    plt.title('Esforços axiais em kN')

    for barra in tabelabarras.index:
        N1, N2, Esf, sen, cos = tabelabarras.loc[barra, ['N1', 'N2', 'Esf', 'sen', 'cos']]
        x1, y1 = tabelanos.loc[N1, ['X', 'Y']]
        x2, y2 = tabelanos.loc[N2, ['X', 'Y']]
        
        if cos != 0:
            tg = sen/cos
            ang = np.arctan(tg)
            ang = 180*ang/np.pi
        else:
            ang = 90
        
        x = [x1, x2]
        y = [y1, y2]
        
        if Esf == 0:
            cor = 'k'
        elif Esf > 0:
            cor = 'r'
        else:
            # Esf < 0
            cor = 'b'
        plt.plot(x, y, cor, zorder=-1)
        
        plt.text(np.mean(x), np.mean(y),
                '{:.2f}kN'.format(Esf/1000),
                rotation=ang,
                horizontalalignment='center',
                verticalalignment='center',
                size = 14,
                weight ='bold'
                )
        
        # Desenhando rotulas
        plt.scatter(x, y, s=40, color='black', marker="o", zorder=0) # 6 é restrição vertical e 5 na horizontal

    print("\n\n\n                                                             Presione 'enter' para prosseguir!\n")
    final = input("                                                                             ")
    # Após todo o pediodo de entrada de informações pelo usuário, exibe o grafico
    plt.figure(1, figsize=(12, 4.5))  # Criando a figura e definindo seu número e tamanho em X e Y
    plt.grid(True)  # Plotando a grade
    plt.title('Cálculo Estrutural de Treliças')
    plt.show()
except Exception as e:
    print("Treliça com ausencia de equilibiro estatico\n\n\n ")
    os._exit(0)

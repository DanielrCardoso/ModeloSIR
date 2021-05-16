from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import os

def dU_dt(U, t):
    #      |         S          |                I                 |      R     |
    return [-alpha * U[0] * U[1], alpha * U[0] * U[1] - beta * U[1], beta * U[1]]

def dU_dt2(U, t):
        #      |         S          |                I                 |      R     |
    return [-alpha * U[0] * U[1], alpha * U[0] * U[1] - beta * U[1], beta * U[1]]

def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getDados():
    alpha = float(input('Informe a taxa de transmissão(Alfa): '))
    beta = float(input('Informe a taxa de recuperação(beta): '))
    populacao = float(input('Informe o tamanho da população(eixo Y): '))
    diasVisualizar = float(input('Numero em dias que deseja visuaizar no grafico(eixo X): '))
    dias = float(input('Numero em dias que deseja rodar a simulação: '))
    return [alpha,beta,populacao,dias,diasVisualizar]

loop = 1
invalido = True
while(loop == 1):
    while(invalido):
        limpa_tela()
        qualSir = int(input('Informe o modelo que deseja usar:\n1 - Modelo SIR\n2 - Modelo SIR 2\n0 - Sair\n'))
        if qualSir > 2:
            limpa_tela()
            print("Informe uma opção valida\n")
            invalido = True
        else:
            invalido = False
    
    limpa_tela()
    alpha,beta,populacao,dias,diasVisualizar = getDados()
    U0 = [populacao, 1, 0] 
    ts = np.arange(0, dias*0.146, 1.4)
        
    if qualSir == 1:
        qualModel = "SIR_"
        Us = odeint(dU_dt, U0, ts)
    elif qualSir == 2:
        qualModel = "SIR_2_"
        Us = odeint(dU_dt2, U0, ts)

    S, I, R = Us[:,0], Us[:,1], Us[:,2]

    fig = plt.subplots(figsize = (20,10), dpi = 80)
    plt.plot(ts, S, label = 'Suscetiveis')
    plt.plot(ts, I, label = 'Infectados')
    plt.plot(ts, R, label = 'Retirados')
    plt.ylim([0, populacao])
    plt.xlim([0, diasVisualizar])
    plt.legend(fontsize = 15)
    
    limpa_tela()
    grafico =qualModel+ "simulacao_"+str(alpha)+"_"+str(beta)+"_"+str(populacao)
    plt.savefig(grafico +".png")
    print("O grafico da simulação foi gerado com o nome: "+grafico+".png\n")
    invalido = True
    loop = int(input("Deseja realizar uma nova simulação:\n1 - Sim\n2 - Não\n"))

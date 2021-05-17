from scipy.integrate import odeint
import numpy
import matplotlib.pyplot as plt
import os

def Modelo_SIR(y,t,alpha,beta):
    S,I,R = y
    ds_dt = -alpha * S * I
    di_dt = alpha * S * I - beta * I
    dr_dt = beta * I
    return([ds_dt, di_dt, dr_dt])

def Modelo_SIR_2(y,t,alpha,beta):
    S,I,R = y
    ds_dt = -alpha * S * I
    di_dt = alpha * S * I - beta * I
    dr_dt = beta * I
    return([ds_dt, di_dt, dr_dt])

def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getDados():
    alpha = float(input('Informe a taxa de transmissão(Alfa): '))
    beta = float(input('Informe a taxa de recuperação(beta): '))
    populacao = float(input('Informe o tamanho da população(eixo Y): '))
    diasVisualizar = float(input('Informe o tempo maximo(eixo X): '))
    populacaoInfec = float(input('Informe o tamanho da população infectada(Recomendado=0.01): '))
    return [alpha,beta,populacao,diasVisualizar,populacaoInfec]

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
    alpha,beta,populacao,diasVisualizar,populacaoInfec = getDados()
    U0 = [populacao, populacaoInfec, 0] #Condicoes iniciais S I R
    t = numpy.linspace(0,100,10000)
        
    if qualSir == 1:
        qualModel = "SIR_"
        solucao = odeint(Modelo_SIR, U0, t,args=(alpha,beta))
    elif qualSir == 2:
        qualModel = "SIR_2_"
        solucao = odeint(Modelo_SIR_2, U0, t,args=(alpha,beta))

    plt.figure(figsize=[20,10])         #Dimensoes da imagem

    plt.plot(t, solucao[:,0], label = 'Suscetiveis')
    plt.plot(t, solucao[:,1], label = 'Infectados')
    plt.plot(t, solucao[:,2], label = 'Retirados')

    plt.ylim([0, populacao])        #gera o eixo Y de 0 ate populacao maxima
    plt.ylabel("População")
    plt.xlim([0, diasVisualizar])   #gera o eixo X de 0 ate dias maximo
    plt.xlabel("Tempo")

    plt.legend(fontsize = 15)       
    
    limpa_tela()
    grafico =qualModel+ "simulacao_"+str(alpha)+"_"+str(beta)+"_"+str(populacao)
    plt.savefig(grafico +".png")
    #plt.show() #abre o grafico
    print("O grafico da simulação foi gerado com o nome: "+grafico+".png\n")
    invalido = True
    loop = int(input("Deseja realizar uma nova simulação:\n1 - Sim\n2 - Não\n"))

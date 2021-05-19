ModeloSIR 
=== 

Este foi um projeto realizado para o trabalho de Cálculo 2 na Universidade de Engenharia do Gama - FGA - UnB. 

## Como funciona? 

O programa gera como base nas equações do modelo SIR um gráfico contendo três curvas: Suscetíveis, Infectados e Retirados. 

## Como instalar 

É necessário ter o compilador do python pip ou semelhante para rodar o projeto. É possível realizar a instalação do compilador python a partir da página oficial da linguagem(https://www.python.org/downloads/). 

 
No terminal, clone o projeto: 

``` 
git clone https://github.com/DanielrCardoso/ModeloSIR 
``` 

Entre na pasta do projeto: 
``` 
cd ModeloSIR 
``` 

Execute o código: 
``` 
Python modeloSIR.py 
``` 
## Utilizando a ferramenta: 
1. Selecione o modelo SIR no menu inicial. 

2. Algumas informações serão solicitadas: 
    - Taxa de transmissão (Alfa). 
    - Taxa de recuperação (Beta). 
    - Tamanho da população 
    - Tempo máximo para visualizar a simulação. 
    - Tamanho da população inicial infectada. 
    
3. Após os passos anteriores um arquivo .png será criado no diretório do programa com o seguinte nome: SIR_simulacao_ValorALFA_ValorBeta_TamanhoDaPopulacao 

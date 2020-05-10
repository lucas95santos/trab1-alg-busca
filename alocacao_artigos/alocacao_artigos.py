"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopes - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""


import csv
import random

#arquivos
inputpath = "./input.txt"
graphic = "fitness.png"
output = "saida-genetico.txt"


#parametros

"""

função de fitness: 
-reflete quão bem adaptado é um individuo
-individuos mais aptos (melhor fitness) tem maior probabilidade de serem 
selecionados para reprodução

tecnica da roleta: 
-cada individuo é dono de uma porção da  roleta
-individuos melhores adapatados (maior fitness) posuem maior chance de serem escolhidos

crossover:
-filhos recebe caracteristicas de cada pai

taxa de crossover é um valor escolhido como ponto de corte para determinar 
se havera ou não cruzamento de dois cromossomos
Tipicamente, taxa de crossover: 0,6 < TC < 1,0
Caso crossover não seja aplicado, os descendentes serão iguais
aos pais

"""

crossover_rate = 0
#mutationra deve ser um valor alpha, onde 0 <= alpha <= m (numero de arquivos a ser revisados)
mutationrate = 1
maxgen = 100


#realiza leitura do arquivo e retorna uma lista de listas 
def read_input_file():
    file_ = open(inputpath, "r")
    reader = csv.reader(file_)
    data = list(reader)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])        
    return data

    
    
#recebe uma lista e escreve no arquivo de saida a solucação encontrada
def write_output_file(s):
    file_ = open(output, 'w')
    writer = csv.writer(file_)
    writer.writerows(s)
    file_.close()
    
"""
    Parâmetros:
    []crossover
    []taxa de mutação
    []maxgen
    
    Processo de seleção por roleta
"""

"""    
    Seu algoritmo deve receber como entrada uma matriz N xM + 1, lida a partir de um arquivo
    textual. Nesta matriz, N é o número de revisores cadastrados e M é o número de artigos a serem
    atribuı́dos. Ao final de cada linha, estará expresso o máximo de artigos que o revisor aceita receber
    (sempre maior ou igual a 1). Abaixo, um exemplo de entrada:
    
    0,0,3,4,4,1
    3,3,0,0,1,2
    4,0,0,1,0,1
    2,2,2,3,2,2   
    
    Neste exemplo, 5 artigos foram recebidos e 4 revisores estão disponı́veis. O revisor 1 tem
    afinidade 0 com os artigos 1 e 2; afinidade 3 com o artigo 3; afinidade 4 com os artigos 4 e 5; e
    aceita receber, no máximo, 1 artigo para revisar.
    
    3,2,1,4,4
    
    Neste exemplo, o artigo 1 foi atribuı́do ao revisor 3; o artigo 2 ao revisor 2; o artigo 3 ao revisor
    1; o artigo 4 ao revisor 4; e o artigo 5 também ao revisor 4.    
    
"""
#geração da populaçao aleatoria
def random_population(data, n, m, number_of_individuals):
    p = [] #lista da população gerada
    for j in range(number_of_individuals):
        new_guy = []
        for s in range(m):
            while len(new_guy) < m:
                x = random.randint(1, n)
                if new_guy.count(x) < data[x-1][m]:
                    new_guy.append(x)
        p.append(new_guy)
    return p

#A função de fitness considera o grau de satisfação dos corretores em relação a distribuição escolhida
def fitness(data, generation):
    f = []
    for k in range(len(generation)):
        soma = 0
        for l in range(len(generation[k])):
            soma += data[generation[k][l]-1][l]
        f.append(soma)
    return f
        
    
    
                

def genetic_algotithm(data, n_individuals):
    
    # n presenta o numero de revisores cadastrados
    n = len(data)
    # m numero de artigos a serem atribuidos
    m = len(data[0])-1
    
    population = random_population(data, n, m, n_individuals)
    
        
    for g in range(maxgen):
        #selecao
        f = fitness(data, population)
     
        #crosover
        
        #mutacao
         

        
    
      
    

if __name__ == '__main__':
    #leitura do arquivo
    data = read_input_file()
    
    for i in range(10):
        #execução do algoritmo genetico
        #solution = genetic_algotithm(data)
        genetic_algotithm(data, 10)
    
        #escrita do arquivo
        #write_output_file(solution)
    
    
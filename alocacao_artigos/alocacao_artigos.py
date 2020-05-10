#!/usr/bin/python3
"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopes - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
        
        Utilizar versão 3.6 do python ou superior para correta execução do programa
"""


import csv
import copy
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

crossover_rate = 0.5
mutationrate = 0.2
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
        
    
def crossover(individuos1, individuos2):
    sons = []
    #calculo dos indices crossover
    limit = int(round(len(individuos1[0])*crossover_rate))
    for i in range(len(individuos1)):
        son1 = individuos1[i][:limit]+individuos2[i][limit:]
        son2 = individuos2[i][:limit]+individuos1[i][limit:]
        sons.append(son1)
        sons.append(son2)
        
    return sons

def select_sons(data, sons, n_individuals):
    F = fitness(data, sons)
    ordained_sons = [x for _,x in sorted(zip(F,sons))]
    #print("sons: ", sons)
    #print("fitness: ", F)
    #print("order:", ordained_sons[n_individuals:], "\n")
    return ordained_sons[n_individuals:]
    
       
def mutation(data, best_sons, n, m, n_individuals):
    kids_mutation = []
    #percorrer individuos
    for i in range(n_individuals):        
        
        #print (int(round((n_individuals)*mutationrate)))
        # percorrer numero de alterções "nos genes"
        for j in range(int(round((n_individuals)*mutationrate))):
            index_visited = []
            while True:
                #gerar possivel indice
                random_index = random.randint(0,m-1)
                #gerar possivel corretor
                random_corretor = random.randint(0, n-1)
                possible_kid = copy.copy(best_sons[i])
                possible_kid[random_index] = random_corretor+1
                
                if (random_index not in index_visited and 
                    possible_kid.count(random_corretor+1) <= data[random_corretor][m] and
                    possible_kid != best_sons[i]):
                    index_visited.append(random_index)
                    kids_mutation.append(possible_kid)                    
                    break
                
    return kids_mutation
                
            

def genetic_algotithm(data, n_individuals):
    
    # n presenta o numero de revisores cadastrados
    n = len(data)
    # m numero de artigos a serem atribuidos
    m = len(data[0])-1
    
    population = random_population(data, n, m, n_individuals)
    
    
    #TODO: estrutura de repetição
    #for g in range(maxgen):
    
    f = fitness(data, population)
        
    #gera pares diferentes
    #seleção por roleta
    #usar python3.6 ou versão mais atualizada
    
    #
    #
    #
    
    
    individuos1 = random.choices(population, weights=f, k=n_individuals)
    individuos2 = random.choices(population, weights=f, k=n_individuals)
    i = 0
    while True:
        if individuos1[i] == individuos2[i]:
            individuos2 = random.choices(population, weights=f, k=n_individuals)
            i = 0
        else:
            i += 1
            if i == len(individuos1):
                break
            
    sons = crossover(individuos1, individuos2)
    

    
    best_sons = select_sons(data, sons, n_individuals)
    print ("Melhores filhos:             ", best_sons)
    
    best_kids_with_mutation = mutation(data, best_sons, n, m, n_individuals)
    print ("Melhores filhos com mutação: ", best_kids_with_mutation)
    
    population = copy.deepcopy(best_kids_with_mutation)
    print ("Population to new iteration: ", population, "\n")
           
    

    

if __name__ == '__main__':
    #leitura do arquivo
    data = read_input_file()
    
    for i in range(10):
        #execução do algoritmo genetico
        #solution = genetic_algotithm(data)
        genetic_algotithm(data, 4)
    
    
    
    #escrita do arquivo    
    #write_output_file(solution)
    
    
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

# arquivos
inputpath = "./input.txt"
graphic = "fitness.png"
output = "saida-genetico.txt"

# parametros

"""
Função de fitness: 
- reflete quão bem adaptado é um individuo.
- individuos mais aptos (melhor fitness) tem maior probabilidade de serem .
selecionados para reprodução.

Técnica da roleta: 
- cada individuo é dono de uma porção da  roleta.
- individuos melhores adapatados (maior fitness) posuem maior chance de serem escolhidos.

Crossover:
- filhos recebem características de cada pai.

Taxa de crossover é um valor escolhido como ponto de corte para determinar 
se havera ou não cruzamento de dois cromossomos
Tipicamente, taxa de crossover: 0,6 < TC < 1,0
Caso crossover não seja aplicado, os descendentes serão iguais
aos pais.

"""

crossover_rate = 0.5
mutationrate = 0.2
maxgen = 100


def reader():
    # Parâmetro r significa que está no modo de leitura (read).
    with open('input.txt', 'r') as file:
        data = [[int(num) for num in line.split(',')] for line in file]

    return data


# recebe uma lista e escreve no arquivo de saida a solucação encontrada
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


# geração da populaçao aleatoria
def random_population(data, reviewer_amount, max_articles, number_of_individuals):
    population = []  # Lista da população gerada.
    for j in range(number_of_individuals):
        new_guy = []
        for s in range(max_articles):
            while len(new_guy) < max_articles:
                random_reviewer = random.randint(1, reviewer_amount)  # Gera um número aleatório de 1 à quantidade de
                # revisores.

                if new_guy.count(random_reviewer) < data[random_reviewer - 1][max_articles]:
                    new_guy.append(random_reviewer)
        population.append(new_guy)
    return population


# A função de fitness considera o grau de satisfação dos corretores em relação a distribuição escolhida
def fitness_func(data, generation):
    fitness = []
    for i in range(len(generation)):
        sum = 0
        for j in range(len(generation[i])):
            reviewer = generation[i][j] - 1
            sum += data[reviewer][j]
        fitness.append(sum)
    return fitness


def crossover(individuos1, individuos2):
    sons = []
    # Cálculo do ponto de corte.
    limit = int(round(len(individuos1[0]) * crossover_rate))
    for i in range(len(individuos1)):
        son1 = individuos1[i][:limit] + individuos2[i][limit:]
        son2 = individuos2[i][:limit] + individuos1[i][limit:]
        sons.append(son1)
        sons.append(son2)

    return sons


def select_sons(data, sons, n_individuals):
    fitness = fitness_func(data, sons)
    sorted_sons = [x for _, x in sorted(zip(fitness, sons))]

    return sorted_sons[n_individuals:]


def mutation(data, best_sons, reviewers_amount, max_articles, n_individuals):
    kids_mutation = []
    # Percorre indivíduos.
    for i in range(n_individuals):

        # Percorre número de alterações "nos genes".
        for j in range(int(round(n_individuals * mutationrate))):
            index_visited = []
            while True:
                # Gera possível índice.
                random_index = random.randint(0, max_articles - 1)
                # Gera possível corretor.
                random_corrector = random.randint(0, reviewers_amount - 1)
                possible_kid = copy.copy(best_sons[i])
                possible_kid[random_index] = random_corrector + 1

                if (random_index not in index_visited and
                        possible_kid.count(random_corrector + 1) <= data[random_corrector][max_articles] and
                        possible_kid != best_sons[i]):
                    index_visited.append(random_index)
                    kids_mutation.append(possible_kid)
                    break

    return kids_mutation


def genetic_algorithm(data, n_individuals):
    # reviewers_amount representa o número de revisores cadastrados.
    reviewers_amount = len(data)
    # max_articles equivale ao número de artigos a serem atribuidos para determinado revisor.
    max_articles = len(data[0]) - 1

    population_evolution = []
    fitness_evolution = []

    population = random_population(data, reviewers_amount, max_articles, n_individuals)

    for g in range(maxgen):

        fitness = fitness_func(data, population)

        population_evolution.append(population)
        fitness_evolution.append(fitness)

        # Gera pares diferentes
        # Seleção por roleta

        individuos1 = random.choices(population, weights=fitness, k=n_individuals)
        individuos2 = random.choices(population, weights=fitness, k=n_individuals)
        i = 0

        # Verifica se o indivíduo não está cruzando com ele mesmo.
        while True:
            if individuos1[i] == individuos2[i]:
                individuos2 = random.choices(population, weights=fitness, k=n_individuals)
                i = 0
            else:
                i += 1
                if i == len(individuos1):
                    break

        sons = crossover(individuos1, individuos2)

        best_sons = select_sons(data, sons, n_individuals)
        print("Best sons:                   ", best_sons)

        best_kids_with_mutation = mutation(data, best_sons, reviewers_amount, max_articles, n_individuals)
        print("Best sons with mutation:     ", best_kids_with_mutation)

        population = copy.deepcopy(best_kids_with_mutation)
        print("Population to new iteration: ", population, "\n")

        return population_evolution, fitness_evolution


if __name__ == '__main__':
    # leitura do arquivo
    data = reader()
    total_evolution = []
    total_fitness = []

    for i in range(10):
        print("Execução: ", i)

        population_ev, fitness_ev = genetic_algorithm(data, 8)
        total_evolution.append(population_ev)
        total_fitness.append(fitness_ev)

    print(total_evolution, '\n')
    print(total_fitness)

    # escrita do arquivo
    # write_output_file(solution)

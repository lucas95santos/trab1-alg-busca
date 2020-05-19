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
import matplotlib.pyplot as plt
import numpy as np

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

total_population_evolution = []
total_fitness_evolution = []


def reader():
    # Parâmetro r significa que está no modo de leitura (read).
    with open('input.txt', 'r') as file:
        matrix = [[int(num) for num in line.split(',')] for line in file]

    return matrix


def writer(content):
    with open('saida-genetico.txt', 'w') as file:
        for listitem in content:
            file.write('%s,' % listitem)

"""
    Parâmetros:
    []crossover
    []taxa de mutação
    []maxgen
    
    Processo de seleção por roleta
"""


# geração da populaçao aleatoria
def random_population(reviewer_amount, articles_amount, number_of_individuals):
    population = []  # Lista da população gerada.
    for j in range(number_of_individuals):
        article_dist = []
        for s in range(articles_amount):
            while len(article_dist) < articles_amount:
                random_reviewer = random.randint(1, reviewer_amount)  # Gera um número aleatório de 1 à quantidade de

                # Verifica se o revisor não tem mais artigos do que ele aceita.
                if article_dist.count(random_reviewer) <= data[random_reviewer - 1][articles_amount]:
                    article_dist.append(random_reviewer)
        population.append(article_dist)
    return population


# A função de fitness considera o grau de satisfação dos corretores em relação a distribuição escolhida
def fitness_func(generation):
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


def select_sons(sons, n_individuals):
    fitness = fitness_func(sons)
    sorted_sons = [x for _, x in sorted(zip(fitness, sons))]

    return sorted_sons[n_individuals:]


def mutation(best_sons, reviewers_amount, articles_amount):
    # Percorre indivíduos.
    for line in range(len(best_sons)):
        for column in range(len(best_sons[0])):
            r = np.random.randint(100)
            if r <= mutationrate*100:
                new_reviewer = random.randint(1, reviewers_amount)
                if best_sons[line].count(new_reviewer) <= data[new_reviewer - 1][articles_amount]:
                    best_sons[line][column] = new_reviewer


def genetic_algorithm(n_individuals):
    # reviewers_amount representa o número de revisores cadastrados.
    reviewers_amount = len(data)
    # articles_amount equivale ao número de artigos cadastrados.
    articles_amount = len(data[0]) - 1

    population_evolution = []
    fitness_evolution = []

    population = random_population(reviewers_amount, articles_amount, n_individuals)

    for g in range(maxgen):

        fitness = fitness_func(population)

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

        best_sons = select_sons(sons, n_individuals)
        print("Best sons:                   ", best_sons)

        mutation(best_sons, reviewers_amount, articles_amount)
        print("Mutated Sons:     ", best_sons)

        population = copy.deepcopy(best_sons)
        print("Population to new iteration: ", population, "\n")

        mutated_fitness = fitness_func(best_sons)
        best_fitness = max(mutated_fitness)
        best_fitness_index = mutated_fitness.index(best_fitness)
        best_individual = best_sons[best_fitness_index]

        fitness_evolution.append(best_fitness)
        population_evolution.append(best_individual)

        total_fitness_evolution.extend(fitness_evolution)
        total_population_evolution.extend(population_evolution)

    plt.plot(fitness_evolution)
    plt.ylabel('Fitness')
    plt.show()


if __name__ == '__main__':
    # leitura do arquivo
    data = reader()
    total_evolution = []
    total_fitness = []

    for i in range(10):
        print("Execução: ", i)

        genetic_algorithm(8)

    best_fitness = max(total_fitness_evolution)
    best_fitness_index = total_fitness_evolution.index(best_fitness)
    best_individual = total_population_evolution[best_fitness_index]

    print(best_fitness)
    print(best_individual)

    writer(best_individual)
    # escrita do arquivo
    # write_output_file(solution)

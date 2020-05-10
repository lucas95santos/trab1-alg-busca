"""
    Nome - RGA:
    Fábio Holanda Saraiva Júnior - 2015.1905.006-2
    Felipe Salles Lopes - 2016.1907.032-4
    Lucas Avanzi - 2016.1907.024-3
    Lucas Antonio dos Santos - 2016.1907.013-8
"""


import pandas as pd

class AlocacaoArtigos:

    def __init__(self, crossoverrate=0.6, mutationrrate=0.02, maxgen=100, inputpath='input.txt'):
        self.generation = 0
        self.repeat = 10
        self.best_solution_by_generation
        self.mean_solutions
        self.best_gen = maxgen
        self.best_generations = []
        self.best_solutions = []

        self.article_reviewer_matrix = self.reader(inputpath)
        self.outputpath = 'saida-genetico.txt'


    def reader(self, inputpath):
        # Parâmetro r significa que está no modo de leitura (read).
        with open('input.txt', 'r') as file:
            matrix = [[int(num) for num in line.split(',')] for line in file]

        return matrix

    def run(self, crossoverrate, mutationrate, maxgen):
        for i in range(self.repeat):
            # TODO

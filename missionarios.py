"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopes - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""

import numpy as np

initial_state = [3, 3, 1]


def son_to_str(s):
    return ' '.join([str(v) for v in s])


# verifica se é o estado final
def is_goal(s):
    return s == [0, 0, 0]


# Esse vetor é o estado da população da margem esquerda do rio, sendo que s[0] (s na posição 0) é o valor de
# missionários na margem esquerda, s[1] é o valor de canibais na margem esquerda e s[2] é o valor do barco na margem
# esquerda, sendo que 1 significa que ele está na margem esquerda e 0 que não está.

# gera filhos
def generate_sons(s):
    list_of_sons = []

    # caminho da margem esquerda para a direita
    if s[2] == 1:
        if s[0] - 1 >= 0 and s[1] - 1 >= 0:
            list_of_sons.append([s[0] - 1, s[1] - 1, 0])
        if s[0] - 2 >= 0:
            list_of_sons.append([s[0] - 2, s[1], 0])
        if s[1] - 2 >= 0:
            list_of_sons.append([s[0], s[1] - 2, 0])
        if s[0] - 1 >= 0:
            list_of_sons.append([s[0] - 1, s[1], 0])
        if s[1] - 1 >= 0:
            list_of_sons.append([s[0], s[1] - 1, 0])

    # caminho da margem direita para a esquerda
    else:
        if s[0] + 1 <= 3 and s[1] + 1 <= 3:
            list_of_sons.append([s[0] + 1, s[1] + 1, 1])
        if s[0] + 2 <= 3:
            list_of_sons.append([s[0] + 2, s[1], 1])
        if s[1] + 2 <= 3:
            list_of_sons.append([s[0], s[1] + 2, 1])
        if s[0] + 1 <= 3:
            list_of_sons.append([s[0] + 1, s[1], 1])
        if s[1] + 1 <= 3:
            list_of_sons.append([s[0], s[1] + 1, 1])

    return list_of_sons


def nodes_family_tree(node, fathers):
    parents = []
    while node != initial_state:
        parents.append(node)
        node = fathers[son_to_str(node)]
    parents.append(initial_state)
    parents.reverse()

    return parents


# Busca em largura
def bfs(start):
    candidates = [start]
    fathers = dict()
    visited = [start]

    while len(candidates) > 0:
        father = candidates[0]
        print("Lista de candidatos: ", candidates)
        del candidates[0]
        print("Visitado: ", father)
        if is_goal(father):
            solution = nodes_family_tree(father, fathers)
            print("Solucao encontrada: ", solution)

        for son in generate_sons(father):
            if son not in visited:
                visited.append(son)
                fathers[son_to_str(son)] = father
                # verificando se o numero de canibais sempre é menor que o de missionarios
                if (son[0] >= son[1] or son[0] == 0 or son[1] == 0) and (
                        3 - son[0] >= 3 - son[1] or 3 - son[0] == 0 or 3 - son[1] == 0):
                    print("Enfileirado: ", son, father)
                    print("")
                    candidates.append(son)


# Busca em profundidade
def dfs(start):
    candidates = [start]
    fathers = dict()
    visited = [start]

    while len(candidates) > 0:
        father = candidates[0]
        print("Lista de candidatos: ", candidates)

        """Na busca em profundidade usa-se pilha, não fila."""
        # del candidates[0]
        print("Visitado: ", father)
        if is_goal(father):
            solution = nodes_family_tree(father, fathers)
            print("Solucao encontrada: ", solution)

        number_of_sons = len(generate_sons(father))
        number_of_sons_visited = 0

        for son in generate_sons(father):
            # if son not in visited:
            if (son not in visited) and not (is_goal(father)):
                visited.append(son)
                fathers[son_to_str(son)] = father

                # verificando se o numero de canibais sempre é menor que o de missionarios
                if (son[0] >= son[1] or son[0] == 0 or son[1] == 0) and (
                        3 - son[0] >= 3 - son[1] or 3 - son[0] == 0 or 3 - son[1] == 0):
                    # Deve-se empilhar, não enfileirar
                    print("Empilhado: ", son, father)
                    print("")
                    candidates.insert(0, son)
                    break
            else:
                number_of_sons_visited += 1

        """ Verifica se todos os filhos foram visitados, se sim:
            Remove o pai da iteração atual - ele esta em candidates[0]
        """
        if number_of_sons == number_of_sons_visited:
            del candidates[0]
            print("Fim de um ramo\n")


def score_function(son, fathers):
    """Calcula a função de avaliação do problema para a busca por A e retorna a soma da heurística e o custo.*

    A heurística usada para esse problema é a Distância de Manhattan, na qual calcula a distância entre o nó atual e o
    nó objetivo.

    A função de custo utilizada para esse problema é 1 por operação. Logo a variável cost_function irá receber o
    número - 1 de pais que um nó tem.
    """

    np_son = np.array(son)  # Transforma a lista em um np array.
    cost_function = len(nodes_family_tree(son, fathers)) - 1
    return np_son.sum() + cost_function


# Busca A*
def a_star(start):
    # Lista de valores da função de avaliação de cada nó.
    # O índice dessa lista equivale ao índice da lista de candidatos.
    node_score_function_value = []
    fathers = dict()
    candidates = [start]
    visited = [start]
    father = candidates[0]
    index = 0

    while len(candidates) > 0:
        print("Candidatos: ", candidates)
        del candidates[index]

        if len(node_score_function_value) > 0:
            del node_score_function_value[index]

        print("Visitado: ", father)
        if is_goal(father):
            solution = nodes_family_tree(father, fathers)
            print("Solucao encontrada: ", solution)

        for son in generate_sons(father):
            if son not in visited and not is_goal(father):
                visited.append(son)
                fathers[son_to_str(son)] = father

                # Verifica se não há mais canibais do que missionários
                if (son[0] >= son[1] or son[0] == 0 or son[1] == 0) and (
                        3 - son[0] >= 3 - son[1] or 3 - son[0] == 0 or 3 - son[1] == 0):
                    print("Enfileirado: ", son, father, "\n")
                    candidates.append(son)
                    node_score_function_value.append(score_function(son, fathers))

        if len(candidates) > 0:
            min_value = min(node_score_function_value)
            index = node_score_function_value.index(min_value)
            father = candidates[index]


if __name__ == '__main__':
    # bfs([3,3,1])
    # dfs([3, 3, 1])
    a_star([3, 3, 1])

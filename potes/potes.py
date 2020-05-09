"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopez - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""

initial_state = [0,0]

def son_to_str(s):
	return ' '.join([str(v) for v in s])

def is_goal(s):
	goal = False
	if s[0] == 4 or s[1] == 4:
		goal = True
	return goal

def generate_sons(s):

	listOfSons = []

	#esvaziar o pote 1
	state = [0, s[1]]
	listOfSons.append(state)

	#esvaziar o pote 2
	state = [s[0], 0]
	listOfSons.append(state)

	#encher o pote 1
	state = [7, s[1]]
	listOfSons.append(state)

	#encher o pote 2
	state = [s[0], 5]
	listOfSons.append(state)

	#verter pote 1 no pote 2
	if s[0] >= 5-s[1]:
		state = [s[0]-(5-s[1]), 5]
	else:
		state = [0, s[1] + s[0]]
	listOfSons.append(state)

	#verter pote 2 no pote 1
	if s[1] <= 7-s[0]:
		state = [s[0]+s[1],0]
	else:
		state = [s[0] + (7 - s[0]), s[1] - (7 - s[0])]
	listOfSons.append(state)

	return listOfSons


def nodes_family_tree(node, fathers):
    parents = []
    while node != initial_state:
        parents.append(node)
        node = fathers[son_to_str(node)]
    parents.append(initial_state)
    parents.reverse()

    return parents

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

def bfs(start):
	candidates = [start]
	fathers = dict()
	visited = [start]

	while len(candidates)>0:
		father = candidates[0]
		print("Lista de candidatos: ", candidates)
		del candidates[0]
		print("Visitado: ", father)
		if is_goal(father):
			res = []
			node = father
			while node != start:
				res.append(node)
				node = fathers[son_to_str(node)]
			res.append(start)
			res.reverse()
			print("Solucao encontrada: ", res)
		
		for son in generate_sons(father):
			if son not in visited:
				print("Enfileirado: ", son, father)
				visited.append(son)
				fathers[son_to_str(son)] = father
				candidates.append(son)

if __name__ == '__main__':
	#bfs([0,0])
	dfs([0,0])

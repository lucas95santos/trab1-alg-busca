"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopes - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""
import math

initial_state = [0,0]

class Node:
	def __init__(self, value, parent=None):
		self.parent = parent
		self.value = value
		
		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
	 	return self.value == other.value

	def __lt__(self, other):
	 	return self.f < other.f

	def __str__(self):
		value = self.value
		out = "[" + str(value)[1:-1] + "]"
		return out
	
	def printWithCost(self):
		value = self.value
		out = "[" + str(value)[1:-1] + "], " + str(self.h)
		return out

################################################################################

def son_to_str(s):
	return ' '.join([str(v) for v in s])

################################################################################

def is_goal(s):
	return s[0] == 4 or s[1] == 4

################################################################################

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

################################################################################

def generate_sons_for_a_star(father):
	listOfSons = []

	#esvaziar o pote 1
	value = [0, father.value[1]]
	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	#esvaziar o pote 2
	value = [father.value[0], 0]
	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	#encher o pote 1
	value = [7, father.value[1]]
	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	#encher o pote 2
	value = [father.value[0], 5]
	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	#verter pote 1 no pote 2
	if father.value[0] >= 5-father.value[1]:
		value = [father.value[0]-(5-father.value[1]), 5]
	else:
		value = [0, father.value[1] + father.value[0]]

	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	#verter pote 2 no pote 1
	if father.value[1] <= 7-father.value[0]:
		value = [father.value[0]+father.value[1],0]
	else:
		value = [father.value[0] + (7 - father.value[0]), father.value[1] - (7 - father.value[0])]
	
	if value != father.value:
		state = Node(value, father)
		cost_function(state, father)
		listOfSons.append(state)

	return listOfSons

################################################################################

def euclidean_distance(currentNode, targetNode):
	distance = math.sqrt(
		math.pow((targetNode[0]-currentNode[0]), 2) +
		math.pow((targetNode[1]-currentNode[1]), 2)
	)

	return round(distance, 2)
			
################################################################################

def cost_function(node, parent=None):
	if (parent):
		node.g = parent.g + 1
	else:
		node.g = 1

	node.h = euclidean_distance(node.value, [4,5])
	node.f = node.g + node.h

################################################################################

def find_solution_path(node):
	path = []
	current_node = node

	while current_node is not None:
		path.append(current_node.value)
		current_node = current_node.parent
	
	return path[::-1]

################################################################################

def nodes_family_tree(node, fathers):
    parents = []
    while node != initial_state:
        parents.append(node)
        node = fathers[son_to_str(node)]
    parents.append(initial_state)
    parents.reverse()

    return parents

################################################################################

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

################################################################################

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

################################################################################

def a_star(start):
	# Criando o nó inicial
	start_node = Node(start)
	cost_function(start_node);
	# lista de nós candidatos
	candidates = [start_node]
	# lista de nós visitados
	visited = [start_node]
	# flag para verificar se o objetivo foi alcançado
	goal_achieved = False

	while len(candidates) > 0 and not goal_achieved:
		current_node = candidates[0]
		# exibindo a lista de candidatos
		if (current_node == start_node):
			print("----------------------------------------------")
		else:
			print("\n----------------------------------------------")
			
		print("Lista de candidatos: [", end="")
		for node in candidates:
			if node == candidates[-1]:
				print(node.value, end="")
			else:
				print(node.value, end=",")

		print("]\n")
		# removendo o nó que está no início da fila
		del candidates[0]
		
		print("Visitado: ", current_node.printWithCost())
		
		if is_goal(current_node.value):
			res = find_solution_path(current_node)
			goal_achieved = True
			print("Solucao encontrada: ", res)
		else:
			# gerando os filhos e adicionando eles na lista de candidatos caso eles
			# não tenham sido visitados e já não estejam na lista
			for son in generate_sons_for_a_star(current_node):
				if son not in visited and son not in candidates:
					candidates.append(son)
					print("Enfileirado: ", son, current_node)

			# ordenando a lista de candidatos de acordo com o menor custo
			candidates = sorted(candidates)
			visited.append(candidates[0])

################################################################################

if __name__ == '__main__':
	#bfs(initial_state)
	#dfs(initial_state)
	a_star(initial_state)

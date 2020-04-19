"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopez - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""


def son_to_str(s):
	return ' '.join([str(v) for v in s])

# verifica se é o estado final
def is_goal(s):
	if s == [0, 0, 0]:
		return True
	else: 
		return False

# gera filhos
def generate_sons(s):
	list_of_sons = []

	#caminho da margem esquerda para a direita
	if s[2] == 1:
		if s[0]-1 >= 0 and s[1]-1 >= 0:
			list_of_sons.append([s[0]-1, s[1]-1, 0])
		if s[0]-2 >= 0:
			list_of_sons.append([s[0]-2, s[1], 0])
		if s[1]-2 >= 0:
			list_of_sons.append([s[0], s[1]-2, 0])
		if s[0]-1 >= 0:
			list_of_sons.append([s[0]-1, s[1], 0])
		if s[1]-1 >= 0:
			list_of_sons.append([s[0], s[1]-1, 0])

	#caminho da margem direita para a esquerda
	else:
		if s[0]+1 <= 3 and s[1]+1 <= 3:
			list_of_sons.append([s[0]+1, s[1]+1, 1])
		if s[0]+2 <= 3:
			list_of_sons.append([s[0]+2, s[1], 1])
		if s[1]+2 <= 3:
			list_of_sons.append([s[0], s[1]+2, 1])
		if s[0]+1 <= 3:
			list_of_sons.append([s[0]+1, s[1], 1])
		if s[1]+1 <= 3:
			list_of_sons.append([s[0], s[1]+1, 1])

	return list_of_sons; 
   






# Busca em largura
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
				#print("Enfileirado: ", son, father)
				#print("")
				visited.append(son)
				fathers[son_to_str(son)] = father
				#verificando se o numero de canibais sempre é menor que o de missionarios
				if (son[0] >= son[1] or son[0] == 0 or son[1] == 0) and (3-son[0] >= 3-son[1] or 3-son[0] == 0 or 3-son[1] == 0):
					print("Enfileirado: ", son, father)
					print("")
					candidates.append(son)




# Busca em profundidade
# A implementar
def dfs():
	return 0;


# Busca A*
# A implementar
def a_star():
	return 0;


if __name__ == '__main__':
	bfs([3,3,1])
	
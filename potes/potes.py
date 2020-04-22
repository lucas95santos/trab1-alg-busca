"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopez - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""


def son2str(s):
	return ' '.join([str(v) for v in s])

def isGoal(s):
	goal = False
	if s[0] == 4 or s[1] == 4:
		goal = True
	return goal

def generateSons(s):

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

def bfs(start):
	candidates = [start]
	fathers = dict()
	visited = [start]

	while len(candidates)>0:
		father = candidates[0]
		print("Lista de candidatos: ", candidates)
		del candidates[0]
		print("Visitado: ", father)
		if isGoal(father):
			res = []
			node = father
			while node != start:
				res.append(node)
				node = fathers[son2str(node)]
			res.append(start)
			res.reverse()
			print("Solucao encontrada: ", res)
		
		for son in generateSons(father):
			if son not in visited:
				print("Enfileirado: ", son, father)
				visited.append(son)
				fathers[son2str(son)] = father
				candidates.append(son)

if __name__ == '__main__':
	bfs([0,0])



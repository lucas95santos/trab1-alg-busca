"""
	Nome - RGA:
	Fábio Holanda Saraiva Júnior - 2015.1905.006-2
	Felipe Salles Lopes - 2016.1907.032-4
	Lucas Avanzi - 2016.1907.024-3
	Lucas Antonio dos Santos - 2016.1907.013-8
"""


import csv

#arquivos
inputpath = "./input.txt"
graphic = "fitness.png"
output = "saida-genetico.txt"


#parametros
crossover = 0
mutationrate = 0
maxgen = 100


"""
    Parâmetros:
    []crossover
    []taxa de mutação
    []maxgen
    
    Processo de seleção por roleta
"""

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
    
    
    

if __name__ == '__main__':
    #leitura do arquivo
    data = read_input_file()
    
    #implementação do algoritmo genetico
    #alguem se candidata???
    #precisa-se de voluntarios
    

    #escrita do arquivo
    write_output_file(data)
    
    
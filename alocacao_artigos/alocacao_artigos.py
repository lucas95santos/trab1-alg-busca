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

"""
k individuos inicias gerados aleatoriamente
seleçao
reprodução
mutação

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

crossover_rate = 0
mutationrate = 0
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

"""
    Conferências cientı́ficas baseiam a seleção de artigos a serem publicados em processos de revisão
    por pares. Nestes, cientistas proeminentes da área da conferência são convidados a contribuir,
    revisando artigos submetidos pelos autores, indicando a aprovação ou rejeição dos mesmos.
    
    Um dos grandes problemas enfrentados pelos organizadores dos eventos, no entanto, consiste na
    atribuição dos artigos aos revisores. Em geral, um processo de votação é feito antes da atribuição,
    no qual os revisores são apresentados ao tı́tulo e ao resumo dos artigos a serem avaliados e atribuem
    uma nota inteira de afinidade entre 0 (não desejo revisar, não conheço o tema do artigo) e 5 (desejo
    muito revisar, sou especialista na área do artigo). Além disso, os revisores indicam quantos artigos,
    no máximo, gostariam de revisar para este evento. O grande desafio consiste em atribuir os artigos
    recebidos aos melhores revisores, buscando sempre respeitar os limites de cada colaborador.

    Elabore uma solução de atribuição de artigos baseada em algoritmos genéticos, implementada
    em Python, para auxiliar este processo. Sua solução deverá atribuir artigos de maneira a maximi-
    zar a afinidade revisor / artigo da distribuição. Nenhum artigo pode ficar sem revisão e deve-se,
    sempre, respeitar o máximo de artigos que um revisor pode receber.
    
    Seu algoritmo deve receber como entrada uma matriz N xM + 1, lida a partir de um arquivo
    textual. Nesta matriz, N é o número de revisores cadastrados e M é o número de artigos a serem
    atribuı́dos. Ao final de cada linha, estará expresso o máximo de artigos que o revisor aceita receber
    (sempre maior ou igual a 1). Abaixo, um exemplo de entrada:
    
    0,0,3,4,4,1
    3,3,0,0,1,2
    4,0,0,1,0,1
    2,2,2,3,2,2   
    
    Neste exemplo, 5 artigos foram recebidos e 4 revisores estão disponı́veis. O revisor 1 tem
    afinidade 0 com os artigos 1 e 2; afinidade 3 com o artigo 3; afinidade 4 com os artigos 4 e 5; e
    aceita receber, no máximo, 1 artigo para revisar.
    
    Na sua solução, deve-se ler uma matriz a partir de um arquivo de entrada, no formato N xM +1,
    como a de exemplo apresentada anteriormente. A codificação genética dos estados deve ser definida
    por você. Você deve inicializar os indivı́duos aleatoriamente. Por isso, 10 repetições devem
    ser feitas para um mesmo problema. Você deverá utilizar os operadores de seleção, mutação e
    crossover. Devem ser parâmetros do seu algoritmo a taxa de crossover (com o nome crossoverrate),
    a taxa de mutação (com o nome mutationrate), o máximo de gerações a serem desenvolvidas (com
    o nome maxgen e valor padrão de 100) e o caminho para o arquivo de entrada da matriz (com o
    nome inputpath). A função de fitness a ser utilizada também deve ser definida por você, devendo
    ser aplicada para o processo de seleção por roleta.
    
    Seu programa deverá gerar um gráfico da evolução da função de fitness ao longo das gerações
    (gráfico de linha, com o nome “fitness.png”). Duas linhas devem estar no gráfico, uma para a
    melhor solução e outra para a média das 10 repetições.
    
    
    Também, deve ser gerado um arquivo “saida-genetico.txt”, reportando o resultado obtido ao
    final da execução que, dentre as 10 repetições, teve a melhor função de fitness. Nesta saı́da, uma
    única linha de tamanho M deve ser gerada, indicando o ı́ndice do revisor atribuı́do a um determi-
    nado artigo. Abaixo, um exemplo de saı́da para o problema de entrada reportado anteriormente.
    
    3,2,1,4,4
    
    Neste exemplo, o artigo 1 foi atribuı́do ao revisor 3; o artigo 2 ao revisor 2; o artigo 3 ao revisor
    1; o artigo 4 ao revisor 4; e o artigo 5 também ao revisor 4.    
    
"""

def genetic_algotithm(data):
    
    # n presenta o numero de revisores cadastrados
    n = len(data)
    # m numero de artigos a serem atribuidos
    m = len(data[0])-1
    #print (n, m)    
    
    

if __name__ == '__main__':
    #leitura do arquivo
    data = read_input_file()
    
    #execução do algoritmo genetico
    #solution = genetic_algotithm(data)
    genetic_algotithm(data)

    #escrita do arquivo
    #write_output_file(solution)
    
    
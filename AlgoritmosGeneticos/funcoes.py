import random

def gene_caixabinaria():
    '''
    Gera um gene váldo para o problema das caixas binárias.
    Return:
        Um valor 0 ou 1.
    '''
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def individuo_caixabinaria(n):
    '''
    Gera um indivíduo para o problema das caixas binárias.
    Argumentos:
        n: número de genes do indivíduo.
    Return:
        Uma lista com N genes. Cada gene é o valor de zero ou um.
    '''
    individuo = []
    for i in range(n):
        gene = gene_caixabinaria()
        individuo.append(gene)
    return individuo

def populacao_caixabinaria(tamanho, n):
    '''
    Cria uma população no problema das caixas binárias.
    Args:
        n:numero de genes de um indivíduo.
        tamanho: tamanho da população.
    Return:
        Uma lista conde cada item é um indivíduo, e cada indíviduo é uma lista com n genes.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_caixabinaria(n))
    return populacao
    

def selecao_roleta_max(populacao, fitness):
    '''
    Seleciona os indivíduos de uma população usando o método da roleta.
    Args:
        populacao: lista com todos os indivíduos da população
        fitness: lista com o valor da função objetivo dos indivíduos da população
    Nota: apenas funciona para problemas de maximização.
    Return:
        População dos indivíduos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_simples(pai, mae):
    '''
    Operador de cruzamento de ponto simples.
    Args:
        pai: uma lista representando um indivíduo.
        mãe: uma lista representando um indivíduo.
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram argumentos.
    '''
    ponto_de_corte = random.randint(1, len(pai)-1)
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2

def mutacao_caixabinaria(individuo):
    '''
    Realiza a mutação de um gene no problema das caixas binárias.
    Args:
        individuo: uma lsita representando um indivíduo no problema das caixas binárias
    Return:
        Um indivíduo com um gene mutado.
    '''
    gene_que_sera_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_que_sera_mutado] = gene_caixabinaria()
    return individuo

def funcao_objetivo_caixabinaria(individuo):
    '''
    Computa a função objetivo no problema das caixas binárias.
    Argumentos:
        individuo lista contendo os genes das caixas binárias.
    Return:
        Um valor representando a soma dos genes do indivíduo.
    '''
    return sum(individuo) + 1

def funcao_objetivo_populacao_caixabinaria(populacao):
    '''
    Calcula a função objetivo para todos os membros de uma população.
    Args:
        populacao: lista com todos os indivíduos da população
    Return:
        Lista de calores representando a fitness de cada indivíduo da população.
    '''

    fitness = []
    for individuo in populacao:
        funcao_objetivo = funcao_objetivo_caixabinaria(individuo)
        fitness.append(funcao_objetivo)
    return fitness
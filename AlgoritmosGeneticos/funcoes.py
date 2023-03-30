#Importações de módulos do Python.




import random




#Funções relacionadas ao "gene":




def gene_caixabinaria():
    '''
    Gera um gene váldo para o problema das caixas binárias.
    Return:
        Um valor 0 ou 1.
    '''
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias
    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.
    Return:
      Um valor entre zero a `valor_max_caixa` (inclusive).
    """
    gene = random.randint(0, valor_max_caixa)
    return gene

def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra




#Funções relacionadas ao indivíduo:





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

def individuo_caixanb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.
    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa
    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """
    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato




#Funções relacionadas a população:




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
    
def populacao_caixanb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.
    Args:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa
    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_caixanb(n_genes, valor_max_caixa))
    return populacao

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao




#Funções relacionadas a seleção:






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

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos indivíduos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados




#Funções relacionadas a cruzamento:





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




#Funções relacionadas a mutação:





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

def mutacao_caixanb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias
    Args:
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa
    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo




#Funções relacionadas a objetivos dos indivíduos:





def funcao_objetivo_caixabinaria(individuo):
    '''
    Computa a função objetivo no problema das caixas binárias.
    Argumentos:
        individuo lista contendo os genes das caixas binárias.
    Return:
        Um valor representando a soma dos genes do indivíduo.
    '''
    return sum(individuo) + 1

def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.
    Args:
      individiuo: lista contendo os genes das caixas não-binárias
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca





#Funções relacionadas ao objetivo da população:





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

def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    Args:
      populacao: lista com todos os individuos da população
    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado



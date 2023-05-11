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


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes



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


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
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
    populacao_selecionada = random.choices(
        populacao, weights=fitness, k=len(populacao)
    )
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


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
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


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2) #k=2 é a quantidade de itens a serem sorteados.
    indice1 = lista_sorteada[0]
    indice2= lista_sorteada[1]

    gene1 = individuo[indice1]
    gene2 = individuo[indice2]

    individuo[indice1] = gene2
    individuo[indice2] = gene1

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


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso        
               
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]

    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
    
    return distancia


def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila
    
    




    
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

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado


def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado



#SUPORTE




def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0

    for pegou_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]

            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item


    return valor_total, peso_total


#FUNÇÕES DEDICADAS AOS EXERCÍCIOS

#SENHA DE TAMANHO VARIÁVEL

def gene_senhavariavel(letras):
    '''Sorteia uma letra para o problema da senha de tamanho variável.
    Args:
        letras: possíveis letras a serem sorteadas.
    Return:
        Uma letra dentro das possíveis a serem sorteadas.
    '''
    return random.choice(letras)



def individuo_senhavariavel(tamanho_max, letras):
    '''Cria um individuo para o problema da senha variável.
    Args:
        tamanho_max: tamanho máximo que a senha pode assumir;
        letras: possíveis letras a serem sorteadas.
    Return:
        Uma lista que representa o individuo.
    '''
    tamanho_individuo = random.randint(3,tamanho_max)
    individuo = []
    for _ in range(tamanho_individuo):
        individuo.append(gene_senhavariavel(letras))
    return individuo

def populacao_inical_senhavariavel(individuo, tamanho_max, letras):
    '''Cria uma população para o problema da senha variável.
    Args:
        individuo: número de individuos da população.
        tamanho_max: tamanho máximo que a senha pode assumir.
        letras possíveis de serem sorteadas.
    Return:
        Uma lista que contem todos os individuos.
    '''
    populacao = []
    for _ in range(individuo):
        populacao.append(individuo_senhavariavel(tamanho_max, letras))
    return populacao


def objetivo_senhavariavel(individuo, senha_verdadeira, peso_da_penalidade):
    '''Computa a funcao objetivo de um individuo no problema da senha.
    Args:
        individiuo: lista contendo as letras da senha;
        senha_verdadeira: a senha que você está tentando descobrir;
        peso_da_penalidade: peso para a diferenca de tamanho entre o individuo e a senha real.
    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    '''
    dif = 0

    for letra_ind, letra_ver in zip(individuo, senha_verdadeira):
        dif += abs(ord(letra_ind) - ord(letra_ver))
    
    diferenca_tamanho = abs(len(individuo) - len(senha_verdadeira))
    dif += peso_da_penalidade * diferenca_tamanho

    return dif


def funcao_objetivo_senhavariavel(populacao, senha_verdadeira, penalidade):
    '''Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
        populacao: lista com todos os individuos da população;
        senha_verdadeira: 
        penalidade: peso para a diferenca de tamanho entre o individuo e a senha real (punição).  
    Return:
      Lista contendo os valores da métrica de distância entre senhas.
    '''
    fitness = []

    for individuo in populacao:
        fitness.append(objetivo_senhavariavel(individuo, senha_verdadeira, penalidade))

    return fitness


def selecao_senhavariavel(populacao, fitness, tamanho_torneio):
    '''Faz a seleção de uma população usando torneio.
        Nota: da forma que está implementada, só funciona em problemas de minimização.
    
    Args:
        populacao: lista com todos os individuos da população.
        fitness: lista com os valores de fitness de cada individuo.
        tamanho_torneio: quantidade de invidiuos que batalham entre si.
    Return:
        Individuos selecionados. Lista com os individuos selecionados com mesmo tamanho do argumento 'populacao'.
    '''
    selecionados = []

    par_populacao_fitness = list(zip(populacao, fitness))

    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        melhor_fit = float('inf')

        for individuo, fit in combatentes:
            if fit < melhor_fit:
                selecionado = individuo
                melhor_fit = fit
        
        selecionados.append(selecionado)
    
    return selecionados



def cruzamento_simples_senhavariavel(pai, mae): 
    '''Operador de cruzamento de ponto simples para o problema da senha variável.
    Args:
        pai: Uma lista representando um individuo.
        mae: Uma lista representando um individuo.
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    '''
    if len(pai) < len(mae):
        ponto_de_corte = random.randint(1, len(pai) - 1)
    else:
        ponto_de_corte = random.randint(1, len(mae) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2



def mutacao_senhavariavel(individuo, letras, tamanho_max):
    '''Realiza a mutação de um gene no problema da senha variável.
    Args:
        individuo: uma lista representado um individuo no problema da senha.
        letras: letras possíveis de serem sorteadas.
        tamanho_max: tamanho máximo que a senha pode assumir.
    Return:
        Um individuo (senha variável) com um gene mutado.
    '''
    if random.random() < .5:
        gene = random.randint(0, len(individuo) - 1)
        individuo[gene] = gene_senhavariavel(letras)
        return individuo
    else:
        novo_tamanho = random.randint(3, tamanho_max)
        if novo_tamanho < len(individuo):
            return individuo[:novo_tamanho]
        else:
            for _ in range(novo_tamanho - len(individuo)):
                individuo.append(gene_senhavariavel(letras))
            return individuo
        

def cria_cidades_astronaurta(n):
    """Cria um dicionário aleatório de cidades com suas posições (x, y, z).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random(), random.random())
    return cidades


def funcao_objetivo_caixabinaria(individuo):
    '''
    Computa a função objetivo no problema das caixas binárias.
    Argumentos:
    individuo lista contendo os genes das caixas binárias.
    Return:
    Um valor representando a soma dos genes do indivíduo.
    '''
    return sum(individuo)

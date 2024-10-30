from itertools import product

def exibir_tabela():
    # Cabeçalho da tabela
    print(f"{'A':<5} {'B':<5} {'C':<5} {'D':<5} {'Cond1':<5} {'Cond2':<5} {'Cond3':<5} {'Satisfeitas':<5}")
    print("-" * 60)
    
    # Todas as combinações possíveis de A, B, C, D
    for A, B, C, D in product([True, False], repeat=4):
        # Avaliação das condições
        cond1 = not A or B
        cond2 = (A or B) <= C
        cond3 = (not A) <= (not C or D)
        
        # Verifica se todas as condições são verdadeiras
        todas_satisfeitas = cond1 and cond2 and cond3
        
        # Exibe cada linha da tabela
        print(f"{A:<5} {B:<5} {C:<5} {D:<5} {cond1:<5} {cond2:<5} {cond3:<5} {todas_satisfeitas}")

exibir_tabela()

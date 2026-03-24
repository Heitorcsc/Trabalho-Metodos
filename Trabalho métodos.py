import math

# equação principal
def f(x):
    return x * math.exp(-x) - 0.25

# derivada
def df(x):
    return math.exp(-x) * (1 - x)


# MÉTODOS NUMÉRICOS 

def bissecao(a, b, tolerancia, max_iteracoes):
    for iteracao in range(1, max_iteracoes + 1):
        x = (a + b) / 2  
        erro = abs(f(x)) 
        
        if erro < tolerancia:
            return x, iteracao, erro
        
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
            
    return x, max_iteracoes, erro


def newton(x0, tolerancia, max_iteracoes):
    x = x0
    for iteracao in range(1, max_iteracoes + 1):
        erro = abs(f(x))
        
        if erro < tolerancia:
            return x, iteracao, erro
    
        derivada = df(x)
        x = x - (f(x) / derivada)
        
    return x, max_iteracoes, erro


def falsa_posicao(a, b, tolerancia, max_iteracoes):
    for iteracao in range(1, max_iteracoes + 1):
        
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        erro = abs(f(x))
        
        if erro < tolerancia:
            return x, iteracao, erro
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
            
    return x, max_iteracoes, erro




print("PROJETO MÉTODOS NUMÉRICOS")


a = 0.0
b = 1.0
x0 = 0.5  
tolerancia = 0.000001
max_iteracoes = 100

print("\n RESULTADO BISSEÇÃO:")
raiz, iteracoes, erro = bissecao(a, b, tolerancia, max_iteracoes)
print("Raiz:", round(raiz, 6))
print("Iterações:", iteracoes)
print("Erro:", round(erro, 8))

print("\nRESULTADO NEWTON:")
raiz, iteracoes, erro = newton(x0, tolerancia, max_iteracoes)
print("Raiz:", round(raiz, 6))
print("Iterações:", iteracoes)
print("Erro:", round(erro, 8))

print("\n RESULTADO FALSA POSIÇÃO:")
raiz, iteracoes, erro = falsa_posicao(a, b, tolerancia, max_iteracoes)
print("Raiz:", round(raiz, 6))
print("Iterações:", iteracoes)
print("Erro:", round(erro, 8))
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2

def multiplicacao(n1, n2):
    return n1 * n2


print("-------calculadora--------")
n1 = float(input("informe um numero: "))
n2 = float(input("informe um numero: "))
operador = input("informe o operador (+,-,/,*): ")

if operador == '+':
    resultado = n1 + n2
    
elif operador == '-':
    resultado = n1 - n2
    
elif operador == '*':
    resultado = n1 * n2
    
else: 
    resultado = n1 / n2
    
    print(f" O Resultado é:{resultado}")
    
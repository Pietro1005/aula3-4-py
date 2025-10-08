print("-------calculadora--------")
n1 = float(input("informe um numero: "))
n2 = float(input("informe um numero: "))

resultado = n1 + n2
print("A soma é: ", resultado)

resultado = n1 * n2
print("a multiplicação é:", resultado)

resultado = n1 - n2
print ("a subtração é:", resultado)

resultado = n1 / n2
print("a divisão é:", resultado)

if (n2 == 0):
    print("Não é possivel dividir por zero")

else:
    resultado = n1 / n2
    print("A divisão é: ", resultado)
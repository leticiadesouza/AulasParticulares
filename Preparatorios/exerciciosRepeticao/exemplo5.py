numero = int(input('Digite um número inteiro positivo: '))
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1
print('O fatorial desse número é ', fatorial)
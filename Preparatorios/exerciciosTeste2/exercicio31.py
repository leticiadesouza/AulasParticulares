# Escolha do tipo da carne
print('1 - File Duplo')
print('2 - Alcatra')
print('3 - Picanha')
tipoCarne = input('Informe o tipo da carne escolhida: ')

# Escolha da quantidade
quantidade = float(input('Informe a quantidade comprada: '))

# Verifica cartao
cartaoTabajara = input('Usara cartao Tabajara (S/N): ')

print('\n\n--------------------------------------------')
print("               CUPOM FISCAL                 ")
print('--------------------------------------------\n')

# Verifica o tipo da carne e calcula o valor bruto
if (tipoCarne == '1'):
    print ('Carne Escolhida: File Duplo')
    if (quantidade <= 5):
        valorBruto = quantidade * 4.9
    else:
        valorBruto = quantidade * 5.8
elif (tipoCarne == '2'):
    print('Carne Escolhida: Alcatra')
    if (quantidade <= 5):
        valorBruto = quantidade * 5.9
    else:
        valorBruto = quantidade * 6.8
else:
    print('Carne Escolhida: Picanha')
    if (quantidade <= 5):
        valorBruto = quantidade * 6.9
    else:
        valorBruto = quantidade * 7.8
print('Valor Bruto', valorBruto)

# Verifica se possui desconto
desconto = 0.0
if (cartaoTabajara == 'S'):
    print('Pagamento com cartao Premium')
    desconto = valorBruto * 0.05
else:
    print('Pagamento nao sera com o cartao Premium')
print('Desconto: ', desconto)
print('Valor a Pagar: ', (valorBruto - desconto))
print('\n--------------------------------------------\n\n')

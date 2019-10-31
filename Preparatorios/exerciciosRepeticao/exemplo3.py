# Validacao do nome
nome = ''
while (len(nome) <= 2):
    nome = input('Informe um nome: ')
    if (len(nome) <= 2):
        print ('O nome deve ter mais de tres letras!')

# Validacao da idade
idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('Informe a idade: '))
    if (idade < 0) or (idade > 150):
        print ('Idade deve estar entre 0 e 150')

# Validacao do salario
salario = 0
while (salario <= 0):
    salario = int(input('Informe o salario: '))
    if (salario <= 0):
        print ('O salario deve ser maior que zero')

# Valida o estado civil
estado_civil = 'A'
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = input('Informe o estado civil: ').upper()
    if ('SCVD'.find(estado_civil) < 0):
        print ('Estado civil deve ser informado como S (solteiro), C (casado),'\
            ' V (viuvo) ou D (divorciado)')

print('Dados registrados com sucesso!')
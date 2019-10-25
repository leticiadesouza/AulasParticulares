x = int(input('digite o preco do primeiro produto: '))
y = int(input('digite o preco do segundo produto: '))
z = int(input('digite o preco do terceiro produto: '))

if (x < y) and (x < z):
    print('compre o produto de valor:', x)
if (z < y) and (z < x):
    print('compre o produto de valor:', z)
if (y < x) and (y < z):
    print('compre o produto de valor:', y)

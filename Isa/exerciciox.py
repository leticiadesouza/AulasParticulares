slr = float(input('digite seu salario: '))

if (slr <= 280):
    print('salario atual:', slr)
    print('20% de aumento')
    print('aumento de:', (slr*0.2))
    print('novo salario:', ((slr*0.2)+slr))
elif (slr > 280) and (slr <= 700):
    print('salario atual:', slr)
    print('15% de aumento')
    print('aumento de:', (slr*1.5))
    print('novo salario:', ((slr*0.15)+slr))
if (slr > 700) and (slr <= 1500):
    print('salario atual:', slr)
    print('novo salario:', ((slr*0.1)+slr))
    

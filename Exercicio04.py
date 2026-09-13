n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1+n2+n3+n4)/4
if media>=6:
 print('Aprovado', media)
else:
 if media>=3:
    print('Exame', media)
 else:
   print('Retido', media)
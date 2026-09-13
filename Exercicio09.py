n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo valor: '))

if n1>n2:
    if n1%n2==0:
     print(n1,'É multiplo do',n2 )
    else:
     print(n1,'Não é multiplo do',n2 )

else:
    if n2>n1:
       if n2%n1==0:
        print(n2,'É multiplo do',n1)
    else:
        print(n2,'Não é multiplo de',n1)

if n1==n2:
  print('Numeros iguais são divisiveis por eles mesmos')

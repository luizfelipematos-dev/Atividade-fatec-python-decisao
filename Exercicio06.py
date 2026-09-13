n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))

if n4>n3:
    print(n1,n2,n3,n4)
else:
    if n4>n2:
        print(n1,n2,n4,n3)
    else:
        if n4>n1:
            print(n1,n4,n2,n3)
        else:
            print(n4,n1,n2,n3)


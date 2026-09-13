A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = ((B**2)-(4*A*C))

if delta < 0:
    print("Não existem raízes reais")
else:
    if delta == 0:
        x1 = -B/(2*A)
        print('Existe uma raiz real', x1)
    else:
        x1 = (-B+delta**0.5)/(2*A)
        x2 = (-B-delta**0.5)/(2*A)
        print('Existem duas raizes reais', x1, x2)
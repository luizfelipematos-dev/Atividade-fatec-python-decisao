tipo_investimento = int(input('Digite o tipo de investimento: '))
valor_investimento = float(input('Digite o valor do investimento: '))

if tipo_investimento==1:
    porcentagem = valor_investimento*0.03
    valor_final = valor_investimento+porcentagem
    print('Valor:', valor_final)


else:
    if tipo_investimento==2:
     porcentagem = valor_investimento*0.05
     valor_final = valor_investimento+porcentagem  
     print('Valor:', valor_final)



    else:
       print('Numero de investimento não encontrado')
       





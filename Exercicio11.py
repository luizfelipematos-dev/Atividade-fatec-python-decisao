preco_atual = float(input('Digite o valor do preco atual: '))
media_mensal = float(input('Digite o valor da media mensal: '))

if preco_atual<30.00 and media_mensal<500:
    porcentagem = preco_atual*0.1
    novo_preco = preco_atual+porcentagem
    

else:
  if preco_atual>=30.00 and preco_atual<80.00 and media_mensal>=500 and media_mensal<1000:
    porcentagem = preco_atual*0.15
    novo_preco = preco_atual+porcentagem


  else:  
   if preco_atual>=80.00 and media_mensal>=1000:
    
    porcentagem = preco_atual*-0.05
    novo_preco = preco_atual+porcentagem

   else:
    novo_preco = preco_atual

print('Novo preco:', novo_preco)


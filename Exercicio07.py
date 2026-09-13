n = int(input("Digite o valor do numero: "))

if n%2==0 and n%3==0:
 print('É divisivel por 2 e por 3')

else:
 if n%2==0:
  print('É divisível por 2')

 else:
  if n%3==0:
   print('É divisivel por 3')

  else:
   print('Ele não é divisivel por 2 ou 3')




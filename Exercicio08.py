hora_inicio = int(input('Digite a hora que o jogo começou: '))
minuto_inicio = int(input('Digite o minuto que o jogo começou: '))
hora_final = int(input('Digite a hora que o jogo acabou: '))
minuto_final = int(input('Digite o minuto que o jogo acabou: '))

inicio = hora_inicio*60+minuto_inicio
fim = hora_final*60+minuto_final

if fim>inicio:
    duracao = fim - inicio
else:
    fim = fim+1440
    duracao = fim - inicio 
horas = duracao//60
minutos = duracao%60

print ('A duração do jogo em horas é:', horas)
print('A duração do jogo em minutos é:', minutos)
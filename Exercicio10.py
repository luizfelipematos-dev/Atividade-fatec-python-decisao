voltas = int(input('Digite o numero de voltas: '))
circuito = float(input('Digite a extensão do circuito: '))
tempo = int(input('Digite a duração em minutos: '))

distancia = circuito*voltas

distancia_km = distancia/1000

tempo_horas = tempo/60

velocidade_media = distancia_km/tempo_horas
print('A velocidade média em km/h é:', velocidade_media)



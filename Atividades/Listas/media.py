vetor = [2.5, 7.5, 10.0, 4.0]
soma = 0
for valor in vetor:
    soma += valor

media = soma / len(vetor) 

proximo_da_media = vetor[0]
menor_distancia = abs(vetor[0] - media)

for valor in vetor:
    distancia_atual = abs(vetor-media)
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        proximo_da_media = valor 

print(f'vetor: {vetor}')
print(f'Media: {media:.2f}')
print(f'Valor mais proximo da media: {proximo_da_media}')








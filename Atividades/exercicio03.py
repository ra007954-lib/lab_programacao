vetor =  []
dado = 0

for d in range(50):
    numero =  int(input('Digite o valor do dado (1 a 6): '))
    vetor.append(numero)

for v in range (50):
    if vetor[v] == 6:
        dado +=1

percentual = (dado / 50) * 100

print('Quantidade: ', dado)
print('Percentual: ',percentual, "%")
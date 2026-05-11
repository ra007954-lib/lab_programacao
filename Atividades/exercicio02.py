vetor = []
for v in range(5):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

x = int(input('Digite o valor que quer buscar'))  

posiçao = -1

for v in range(5):
    if vetor [v] == x:
        posiçao = v
        break

print(posiçao)     
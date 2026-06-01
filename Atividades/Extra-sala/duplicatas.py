numeros = []
for i in range(6):
    num = int(input('Digite o {i+1}. numero: '))
    numeros.append(num)

x = int(input('\nQual o número deseja pesquisar? '))
ocorrencias = numeros.count(x)
print("-"*30)
if ocorrencias >0:
    print(f'O numero {x} aparece {ocorrencias} vez(es) na lista.')
    print(f'Sua primeira aparição foi no indice: {numeros.index(x)}')
else:
    print(f'O numero {x} nao foi encontrado na lista.')


           
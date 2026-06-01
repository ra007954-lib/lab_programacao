notas =[]
for i  in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
menor_nota = min(notas)
notas.remove(menor_nota)
print(f'A menor nota removida foi: {menor_nota} ')
print(f'Notas que restaram no sistema: {notas}')

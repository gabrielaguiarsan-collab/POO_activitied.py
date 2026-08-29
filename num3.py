nome = input("Digite o nome do aluno: ")

notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média do aluno {nome} é: {media:.2f}")
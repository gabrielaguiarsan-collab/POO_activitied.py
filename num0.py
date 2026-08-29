vetor = []

for i in range(10):
    numero=int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

print("Números digitados: ")
for i in range(10):
    print(vetor[i])
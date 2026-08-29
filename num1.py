

funcionarios = ["Gabriel", "Gaby", "Matheus", "Pedro", "Pablo"]
print("funcionarios atuais:" , funcionarios)
indice = int(input("Digite o índice do funcionário que deseja remover: "))
nome_funcionario = input("Digite o nome do funcionário substituto: ")
funcionarios[indice] = nome_funcionario
print("funcionarios atualizados:" , funcionarios)
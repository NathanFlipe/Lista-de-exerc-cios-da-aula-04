
aluno = str(input("Nome do aluno: "))
if aluno == "":
    print("Erro!")
    exit("Você não inseriu nenhum nome, tente novamente.")
else:
    print(f"Insira as 3 notas do aluno {aluno} para obter a média.")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

print(f"O aluno {aluno}, obteve a média: {(nota1 + nota2 + nota3) / 3}")
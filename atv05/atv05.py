pedirN = int(input("digite o numero de alunos: "))
somamedia = 0
for i in range(pedirN):
    print(f"\nAluno {i + 1}:")
    nome = input('digite o nome do aluno: ')
    nota1 = float(input('digite a nota do aluno: '))
    nota2 = float(input('digite a nota do aluno: '))
    nota3 = float(input('digite a nota do aluno: ' ))
    soma = nota1 + nota2 + nota3
    media = soma / 3
    somamedia +=media
    print(f"aluno: {nome} notas: {nota1}, {nota2}, {nota3}. media: {media}")
    if media >= 7:
        print(f"aluno {nome} aprovado!")
    else:
        print(f'{nome} reprovado')

mediageral = somamedia / pedirN
print(f"media da turmamamama: {somamedia}")


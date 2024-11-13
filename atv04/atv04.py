inicio = int(input('digite o valor inicial: '))
fim = int(input('digite o valor final: '))

pares = []

soma = 0


for i in range(inicio, fim):
    if i % 2 == 0:
        pares.append(i)
        print(f'os numeros pares são: {pares}')
        soma += i
if pares:
    print(f"a soma dos pares é de: {soma}")
else:
    print('não há pares aqui tchola')
pedirnumero = int(input('digite um numero: '))


if pedirnumero < 0:
    print(f"{pedirnumero} é negativo")
elif pedirnumero == 0:
    print(f"{pedirnumero} é igual a zero")
else:
    print(f'{pedirnumero} é positivo')
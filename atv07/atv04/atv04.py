import random

def advinhacao():
  numero_secreto = random.randint(1, 20)

  while True:
    pedir = int(input("digite um numero de 1 a 20: "))
    if pedir == numero_secreto:
      print("você acertou!")
    else:
      print("errou")


advinhacao()
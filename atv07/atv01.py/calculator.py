from calcs import somar_numeros, subtrair_numeros, multiplicar_numeros, dividir_numeros


while True:
  menu = input("""
escolha o que você deseja fazer: 
1. Somar
2. subtrair
3. dividir
4. multiplicar
0. sair
""")
  match menu:
    case "0":
      print("saindo...")
      break
    case "1":
      try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(f"o resultado da soma é: {somar_numeros(num1, num2)}")
      except ValueError:
        print("erro: você precisa digitar um número")
    case "2":
      try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(f"o resultado da soma é: {subtrair_numeros(num1, num2)}")
      except ValueError:
        print("erro: você precisa digitar um número")
    case "3":
      try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(f"o resultado da soma é: {dividir_numeros(num1, num2)}")
      except ValueError:
        print("erro: você precisa digitar um número")
    case "4":
      try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(f"o resultado da soma é: {multiplicar_numeros(num1, num2)}")
      except ValueError:
        print("erro: você precisa digitar um número")

from atv03 import areaperimetro_triangulo, areaperimetro_circulo, areaperimetro_quadrado


while True:
  menu = input("""
  escolha o que quer calcular:
  1. quadrado
  2. circulo
  3. triangulo
  0.sair
  """)
  match menu:
    case "0":
      print("saindo...")
      break
    case "1":
      print(areaperimetro_quadrado())
    case "2":
      print(areaperimetro_circulo())
    case "3":
      print(areaperimetro_triangulo())

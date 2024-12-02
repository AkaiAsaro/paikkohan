import math

def areaperimetro_triangulo():
  while True:
    a = float(input("digite um numero do triãngulo: "))
    b = float(input("digite um numero do triãngulo: "))
    c = float(input("digite um numero do triãngulo: "))
    soma = a + b + c
    s = soma / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    perimetro = a + b + c
  
    return f"area do triangulo é igual a {area}, perimetro é igual a: {perimetro}"


def areaperimetro_quadrado():
  lado = float(input("digite o lado do quadrado: "))
  area = lado**2
  perimetro = 4 * lado
  return f"a area do quadrado é igual a {area}, o perimetro é igual a {perimetro}"

def areaperimetro_circulo():
  raio = float(input("digite o raio do circulo: "))
  area = math.pi * raio ** 2
  perimetro = 2 * math.pi * raio
  return f"a area do circulo é de {area}, o perimetro é de {perimetro}"
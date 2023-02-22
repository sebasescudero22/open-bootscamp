def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b

      
      from modulos.calculadora import sumar, restar, multiplicar, dividir

resultado = sumar(5, 3)
print("Suma:", resultado)

resultado = restar(5, 3)
print("Resta:", resultado)

resultado = multiplicar(5, 3)
print("Multiplicación:", resultado)

resultado = dividir(5, 3)
print("División:", resultado)

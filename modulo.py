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



//modulo con scrpt de tiempo


import time

def hora_de_irse():
    hora_actual = time.localtime().tm_hour
    minutos_actuales = time.localtime().tm_min
    
    if hora_actual >= 19:
        print("¡Hora de irse a casa!")
    else:
        minutos_restantes = (19 - hora_actual - 1) * 60 + (60 - minutos_actuales)
        print(f"Aún no es hora de irse a casa. Quedan {minutos_restantes} minutos de trabajo.")

hora_de_irse()


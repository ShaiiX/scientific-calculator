import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es pot dividir entre zero."

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: No es pot calcular la arrel quadrada d'un número negatiu."

def logaritmo(a):
    if a > 0:
        return math.log(a)
    else:
        return "Error: No es pot calcular el logaritme d'un número no positiu."

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def exponencial(a):
    return math.exp(a)

def pi():
    return math.pi

def euler():
    return math.e

print("Calculadora Científica")
print("Operacions disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicació")
print("4. Divisió")
print("5. Potència")
print("6. Arrel quadrada")
print("7. Logaritme")
print("8. Sinus")
print("9. Cosinus")
print("10. Tangent")
print("11. Exponencial")
print("12. Pi")
print("13. Euler")

opcion = input("Ingressa el número corresponent a l'operació que vols realitzar: ")

if opcion in ['1', '2', '3', '4', '5']:
    num1 = float(input("Ingressa el primer número: "))
    num2 = float(input("Ingressa el segon número: "))
    if opcion == '1':
        print("Resultat:", suma(num1, num2))
    elif opcion == '2':
        print("Resultat:", resta(num1, num2))
    elif opcion == '3':
        print("Resultat:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultat:", division(num1, num2))
    elif opcion == '5':
        print("Resultat:", potencia(num1, num2))
elif opcion in ['6', '7', '8', '9', '10', '11']:
    num = float(input("Ingressa el número: "))
    if opcion == '6':
        print("Resultat:", raiz_cuadrada(num))
    elif opcion == '7':
        print("Resultat:", logaritmo(num))
    elif opcion == '8':
        print("Resultat:", seno(num))
    elif opcion == '9':
        print("Resultat:", coseno(num))
    elif opcion == '10':
        print("Resultat:", tangente(num))
    elif opcion == '11':
        print("Resultat:", exponencial(num))
elif opcion == '12':
    print("Resultat:", pi())
elif opcion == '13':
    print("Resultat:", euler())
else:
    print("Opció no vàlida. Si us plau, ingressa un número de l'1 al 13 per sel·leccionar una operació vàlida.")

input("Pressiona Enter per sortir...")
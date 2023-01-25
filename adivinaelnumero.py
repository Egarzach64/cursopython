# Este es el Juego para adivinar el Numero
import random

intentos = 0

print("hola, Cual es tu Nombre: ?" )
miNombre = input()

numero = random.randint(1,20)
print("Bueno," + miNombre + " intenta adivinar un nomero entre 1 y 20.")

while intentos < 6:
    print("Intenta adivinar...")
    adivinanum = input()
    adivinanum = int(adivinanum)

    intentos = intentos + 1

    if adivinanum < numero:
       print("Tu numero es Menor que el mio...")

    if adivinanum > numero:
       print("Tu numero es Mayor que el mio...")   

    if adivinanum == numero:
       break

if adivinanum == numero:
    intentos = str(intentos)
    numero = str(numero)
    print("Has adivinado..." + miNombre + " el numero: " + numero + " en " + intentos + " Realizados")

if adivinanum != numero:
    intentos = str(intentos)
    numero = str(numero)
    print("Has Fallado..." + miNombre + " el numero era : " + numero + " y no lo divinaste en " + intentos + " intentos Realizados")

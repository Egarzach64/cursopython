import random
numero1 = random.randint(1, 20)
numero2 = random.randint(1, 20)
print('¿Cuánto es la suma de ' + str(numero1) + ' + ' + str(numero2) + '?')
respuesta = input()
if int(respuesta) == numero1 + numero2:
   print('¡Correcto!')
else:
   print('¡Nops! La respuesta es ' + str(numero1 + numero2))


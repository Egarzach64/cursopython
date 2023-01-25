import random
print('Lanzaré una moneda 1000 veces. Adivina cuantas veces caerá Cara. (Presiona enter para comenzar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
   valor = random.randint(0, 1)
   #print(lanzamientos,valor)  
   if int(valor) == 1:
      caras = caras + 1
   lanzamientos = lanzamientos + 1

   if lanzamientos == 100:
      print('100 lanzamientos y hubo ' + str(caras) + ' caras.')
   if lanzamientos == 500:
      print('En 500 lanzamientos, cara salió ' + str(caras) + ' veces.')
   if lanzamientos == 900:
      print('en 900 lanzamientos y cara salió ' + str(caras) + ' veces.')
      print()
      print('De 1000 lanzamientos, al final cara salió ' + str(caras) + ' veces!')
      print('¿Estuviste cerca?')

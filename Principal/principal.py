#Integrantes
#David Santiago Pirateque
#Juan Daniel Hurtado  
#David Santiago Rodriguez
import time
contador=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print('LA FRASE FINAL\n')
time.sleep(1)
print("Iniciamos...\n")
time.sleep(1.8)
def Inicio ():
  print("De repente sientes la luz de una lámpara sobre tu cara, demoras unos segundos en recoradar quien eres...")
  nombre = input("Mi nombre es: ")
  fin = False
  while fin == False:
      decision = input("¿Seguro que es tu nombre?\n")
      if decision == "si" or decision == "SI" or decision == "Si":
          fin = True
      elif decision == "no" or decision == "NO" or decision == "No":
          nombre = input("Mi nombre es: ")
      else:
          print("Comando no válido")
  return nombre
nombre = Inicio()
        
i = 0
n = 0


from Cuchillo import Herramienta1
from Linterna import Herramienta2
from Llave import Herramienta3

def herramienta(i,contador):
  print(f"\n{nombre} te despiertas en medio de una habitacion, a tu lado puedes ver una mesa con tres objetos. Te levantas y miras en detalle que es, te das cuenta que hay un cuchillo, una linterna y lo que parece una llave.\n\nSolo puedes escoger uno ¿Cuál eliges?\nA.Cuchillo\nB.Linterna\nC.Llave")
  tool = input()
  i += 1
  if tool == "A" or tool == "a":
      print("Escogiste Cuchillo\nPreparate...\n")
      time.sleep(3)
      Herramienta1.Cuchillo(contador)
      restart(i,contador)
  elif tool == "B" or tool == "b":
      print("Escogiste Linterna \nPreparate...")
      time.sleep(3)
      Herramienta2.linterna(n,contador)
      restart(i,contador)
  elif tool == "C" or tool == "c":
      print("Escogiste Llave\nPreparate...")
      time.sleep(3)
      Herramienta3.Llave(i,contador)
      restart(i,contador)
  else:
      if i != 3:
          print(" ")
          print("Elección no valida, Digita nuevamente la opción")
          print(" ")
          herramienta(i,contador)
      elif i == 3:
          print(
              "Usted no quiere jugar, no joda y vaya a hacer algo más productivo con su vida"
          )
          contador[33]+=1
          restart(i,contador)

i = 0
def restart(i,contador):
  indicador=""
  sanidad=True
  y=0
  for x in contador:
    if x == 10:
      print ("¿Enserio le quedó grande conseguir más finales? Pues 10 veces el mismo resultado no es de alguien normal....")
      x+=1
      contador[34]+=1
      print(" ")
  for x in contador:
    if x >30:
      print ("Vaya a hacer algo con su vida. Estudie, báñese o sea alguien productivo, pero no joda que lo que lleva acá ya es enfermizo")
      contador[35]+=1
      print(" ")
  for x in contador:
    if x == 50:
      print ("Chao. Le vamos a hacer un favor a su miserable existencia y hasta acá llega el juego. ¿50 veces el mismo final? Más bien hágase revisar por un psiquiatra que eso si está preocupante.")
      sanidad=False
  for x in contador:
    y+=x
  if y==99:
    print ("Wow, eso si que se le llama perseverancia. Ni nosotros esperábamos que alguien se gastara tanto tiempo acá")
    contador[36]+=1
  for x in contador:
    if x == 0:
      indicador+="\u274C"
    if x != 0:
      indicador+="\u2705"
  print(indicador)
  if sanidad==True:
    a=False
    while a==False:
      print("\n¿Deseas volver a probar suerte con tu destino?")
      restart=input()
      if restart == "Si" or restart == "si" or restart == "SI":
        a=True
        i=0
        herramienta(i,contador)
      if restart == "No" or restart == "no" or restart == "NO":
        print("Gracias por participar :v")
        a = True
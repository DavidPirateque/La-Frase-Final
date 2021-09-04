#Llave
from Llave import Puertas

def Llave(i,contador):
  a= False
  while a == False:
    print ("\nSuena una alarma que retumba en las paredes y no te deja pensar bien, lo único que sabes es que tienes que salir de ahí, sales y encuentras un pasillo oscuro, lleno de puertas cerradas. A tu derecha y a tu izquierda hay una, pero más adelante ves que siguen apareciendo puertas por las cuales girar\n\n¿Que te espera detrás de cada una?\n\nA.Derecha\nB.Izquierda\nC.Seguir adelante") 
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      Puertas.infierno(eleccion,contador)
      a=True
    if eleccion == "B" or eleccion == "b":
      Puertas.MonstersINC(eleccion,contador)
      a= True
    if eleccion == "C" or eleccion == "c":
      pasillo0(eleccion,contador)
      a=True
  
def pasillosub(eleccion,contador):
  b=False
  while b == False:
    print("\nA tu derecha y a tu izquierda hay una puerta, pero más adelante ves que siguen apareciendo puertas por las cuales girar\n\n¿Que te espera detrás de cada una?\n\nA.Derecha\nB.Izquierda\nC.Seguir adelante") 
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      Puertas.infierno(eleccion,contador)
      b=True 
    if eleccion == "B" or eleccion == "b":
      Puertas.MonstersINC(eleccion,contador)
      b=True
    if eleccion == "C" or eleccion == "c":
      pasillo0(eleccion,contador)
      b=True
def pasillo0(eleccion,contador):
  c=False
  while c==False:
    print("\nVuelves a encontrarte con una puerta a tu derecha y otra a tu izquierda. Además ves que el pasillo sigue unos cuantos metros más, ves dos puertas al fondo.\n\n¿Que te espera detrás de cada una?\n\nA.Derecha\nB.Izquierda\nC.Seguir adelante\nD.Devolverte") 
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      Puertas.telafumasteperoverde(eleccion,contador)
      c=True
    if eleccion == "B" or eleccion == "b":
      Puertas.mundodepiedra(eleccion,contador)
      c=True
    if eleccion == "C" or eleccion == "c":
      pasillo1(eleccion,contador)
      c=True
    if eleccion == "D" or eleccion == "d":
      pasillosub(eleccion,contador)
      c=True

def pasillo1(eleccion,contador):
  d=False
  while d == False:
    print("\nLlegas al final del pasillo, solo hay dos puertas, una a tu izquieda y la otra a tu derecha.\n\nA.Derecha\nB.Izquierda\nC.Devolverte")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      Puertas.ruben0(eleccion,contador)
      d=True
    if eleccion == "B" or eleccion == "b":
      Puertas.ruben1(eleccion,contador)
      d=True
    if eleccion == "C" or eleccion == "c":
      pasillo0(eleccion,contador)
      d=True
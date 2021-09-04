
from Cuchillo import Bosque 

def Cuchillo (contador):
 momento = False 
 while momento == False: 
    eleccion = input('Recuerdas que estás en 1962, abres la puerta y te encuentras en medio de un refugio de guerra en Vietnam, no alcanzas a respirar y un general te está gritando: “LOS ARROCEROS NOS ESTÁN INVADIENDO, AYUDE A DEFENDER A SU GENTE”, Tienes dos opciones:\n1. Ir a la armería\n2. Ir al bosque\n')
    if eleccion == '1':
      print("\nVas corriendo a la armería a equiparte para la guerra, pero en el momento en que abres la puerta solo ves un destello de luz y escuchas una gran explosión, todo se vuelve oscuro.(Acabas de convertirte en un orgullo para tu país, pero nadie te recordará, luchaste en vano, tal vez si hubieras elegido sabiamente tu destino hubiera sido mejor).\n")
      contador[0]+=1
      momento = True
    elif eleccion == '2':
      momento = True
      Bosque.Ir_Bosque(eleccion,contador)
      










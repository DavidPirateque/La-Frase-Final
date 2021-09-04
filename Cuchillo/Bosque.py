
from Cuchillo import Rio
def Ir_Bosque(eleccion,contador):
    momento = False
    while momento==False:
      eleccion = input("\nEscuchas los disparos del enemigo y los gritos de tus amigos, ves que hay un río que atraviesa el campamento, Tienes dos opciones:\n1. Lanzarte al rio\n2. Esconderse entre los matorrales\n")
      if eleccion == "1":
        momento = True
        Rio.Lanzarse_Rio(eleccion,contador)
      elif eleccion == "2":
        print('\nMientras corres a esconderte caes en una trampa de los guerrilleros y quedas empalado sufriendo lentamente hasta morir como una victima más del asalto (Mira por donde caminas).\n')
        contador[1]+=1
        momento = True
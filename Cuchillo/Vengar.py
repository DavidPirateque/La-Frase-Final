import time
def Vengar_Amigos(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion= input('Miras por qué camino se va la camioneta y decides seguir las huellas de sus ruedas, caminas tras ese rastro durante todo el día hasta que llegas a una granja de cerdos donde puedes ver las camionetas estacionadas, Tienes dos opciones:\n1. Entras directamente a la casa\n2. Decides recorrer primero el establo\n')
    if eleccion == '1':
      print('En toda la entrada se encontraban tres guardias armados. Abren fuego\n(Haz muerto, tu cadáver es llevado al establo y sufres el mismo destino que tus compañeros)\n')
      contador[5]+=1
      momento = True
    elif eleccion == '2':
      momento = True
      Recorrer_Establo(eleccion,contador)


def Recorrer_Establo(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion= input('\nVes que hay unos cerdos comiendo, al lado están los uniformes de tus compañeros, no le das mucha importancia y sigues en busca de un arma, Tienes dos opciones:\n1. Entras sigilosamente por la parte de atrás de la casa\n2. Entras a dar guerra\n')
    if eleccion == '1':
      print('\nEncuentras un encendedor el cual usas para prender fuego a la madera. Sabes que este es el final pero sientes paz por vengar a tus camaradas\n(El fuego te consume junto a la casa y los guerrilleros. Nadie nunca entenderá lo que en realidad sucedió pero en el fondo puedes descansar en paz).\n')
      contador[6]+=1
      momento = True
    elif eleccion == '2':
      print('\nLogras matar al primer guardia pero los otros dos te fusilan\n(Por ser tan impulsivo no pensaste bien las cosas ahora tienes que atenerte a las consecuencias).\n')
      contador[7]+=1
      momento = True
      
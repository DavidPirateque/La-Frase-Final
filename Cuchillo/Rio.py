from Cuchillo import Ir_Cuchillo
import time 
def Lanzarse_Rio(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion = input('\nSaltas río y al caer te golpeas con una piedra, quedas inconsciente Despiertas y sientes un olor a leña quemada, tus ojos pesan pero cuando logras abrirlos, ves a un hombre robusto que está pescando en el río, te alegras de estar vivo, pero cuando te intentas mover te das cuenta que estás atado de muñecas y tobillos, ves que el cuchillo está a tu alcance, Tienes dos opciones:\n1. Vas por el cuchillo\n2. Te haces el muerto\n')
    if eleccion == '1':
      momento = True 
      Ir_Cuchillo.Ir_por_Cuchillo(eleccion,contador)
    elif eleccion == '2':
      print('\nUn escuadrón de viet-cong que estaba aliado con el hombre que te ató te montan a su camioneta para llevarte a una granja de cerdos donde te arrojan con el resto de cadáveres de tu tropa como alimento para los cerdos. El golpe fue tan fuerte que desmallas\n(Los cerdos te comen vivo. Para tu país eres un desaparecido más en combate, nadie nunca sabrá tu historia).\n')
      contador[2]+=1
      momento = True
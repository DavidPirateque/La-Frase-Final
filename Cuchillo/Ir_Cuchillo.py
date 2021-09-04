from Cuchillo import EsperaryContinuar, Vengar
import time
def Ir_por_Cuchillo(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion = input("\nSales corriendo a coger el cuchillo, el hombre que pesca se da cuenta y en el forcejeo por el cuchillo logras enterrárselo en una pierna, te desatas y corres sin saber a donde te diriges, luego de correr por un largo tiempo, escuchas que unos vehículos se acercan a donde estás, piensas que es tu equipo pero alcanzas a ver la estrella amarilla de viet-cong a un costado de sus camionetas, te escondes entre la maleza y alcanzas a ver los cuerpos sin vida de tus amigos en el platón de la camioneta, Tienes dos opciones:\n1. Vengar a tus amigos\n2. Esperar en silencio y continuar\n")
    if eleccion == '1':
      momento = True
      Vengar.Vengar_Amigos(eleccion,contador)
    elif eleccion == '2':
      momento = True 
      EsperaryContinuar.Esperar_Continuar(eleccion,contador)
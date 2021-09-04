import time
def Esperar_Continuar(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion = input('\nDecides devolverte ya que tienes mucha hambre y te faltan energía, en el camino encuentras la casa del pescador, al llegar no ves al pescador por ninguna parte y decides tomar sus cosas, encuentras un plato de arroz junto a un pedazo de pescado cocinado pero frio, una caña para pescar, una cuerda, ¿qué escoges?:\n1. Arroz y Pescado\n2. Caña de pescar\n3. Cuerda\n')
    if eleccion == '1':
      print('\nComo llevas tiempo sin comer, tomas el arroz con mucha prisa notas que tiene un sabor peculiar, no le das importancia solo hasta que sientes un dolor perforante en el estómago, para entonces es demasiado tarde\n(Has sido intoxicado con un veneno para ratas que había colocado el pescador para controlar las pestes un su zona. Sobreviviste a la guerra pero moriste de la manera mas absurda).\n')
      contador[3]+=1
      momento = True
    elif eleccion == '2':
      print('\nIntentas saber como funciona, sin querer gastas todo tu tiempo en esto. Llega el pescador a buscar sus cosas, te ve sentado con la caña, aprovecha la cuerda y te estrangula\n(Has muerto, la próxima vez vigila en que gastas tu tiempo).\n')
      contador[4]+=1
      momento = True 
    elif eleccion == '3':
      Cuerda(eleccion,contador)
      momento = True
      

def Cuerda(eleccion,contador):
  momento = False
  while momento == False:
    time.sleep(2)
    eleccion = input('\nTomas la cuerda, escuchas pasos acercándose a la casa; te escondes en un rincón de la casa y tratas de respirar en silencio y hacer el menor ruido posible, pasados unos 5 minutos crees que ya no hay nadie, te preparas para salir pero en ese momento el pescador entra, te abalanzas sobre él, y con todas tus fuerzas logras ahorcarlo con la cuerda. Como ya no estás en peligro tienes mas tiempo para elegir que llevarte:\n1. Arroz y Pescado\n2. Caña de pescar\n')
    if eleccion == '1':
      print('\nComo llevas tiempo sin comer, tomas el arroz con mucha prisa notas que tiene un sabor peculiar, no le das importancia solo hasta que sientes un dolor perforante en el estómago, para entonces es demasiado tarde\n(Has sido intoxicado con un veneno para ratas, que había colocado el pescador para controlar las pestes un su zona, sobreviviste a la guerra pero moriste de la manera mas absurda)\n')
      contador[3]+=1
      momento = True
    elif eleccion == '2':
      print('\nIntentas saber como funciona, sin querer gastas todo tu tiempo en esto. Llega el pescador a buscar sus cosas, te ve sentado con la caña, aprovecha la cuerda y te estrangula\n(Has muerto, la próxima vez vigila en que gastas tu tiempo)\n')
      contador[4]+=1
      momento = True 
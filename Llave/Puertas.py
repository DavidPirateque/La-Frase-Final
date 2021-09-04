
import time
i = 0
def infierno (eleccion,contador):
  print("\nEntras y te encuentras en un batalla de rap entre el diablo y un rapero venezolano, todo esto por el alma de su padre, entre todo el ruido de los gritos de sufrimiento, escuchas:")
  time.sleep(1)
  print("\nAntes que nada te maldigo, voy a hacer que sufras el peor de todos los castigos” en ese momento surge te agarra por los tobillos, y te hunde en lo mas profundo de la candela junto a Mao, Che Guevara Y Juan Pablo Segundo. Has muerto\n\nRecitando versos entre fuego y heces, puede que le ganes al jefe.\n")
  contador[21]+=1 

def MonstersINC(eleccion,contador):
  a = False
  while a == False:
    print("\nAbres la puerta y notas que estás en la mitad de una planta de energía donde los trabajadores son criaturas como ninguna que hayas visto, se podría decir que son monstruos. A tu izquierda ves a una bola verde gritando : “Pon esa cosa horrorosa ahí, o veras”, en ese instante todas las criaturas se percatan de tu presencia; de la nada ves una masa amarilla cayendo sobre ti justo cuando una langosta gigante oprime un botón rojo y gritar :33-12 TENEMOS UN 33-12...\n")
    time.sleep(3)
    print("\nMientras aproximadamente 3 monstruos te están llevando a donde una araña gigante, un oso azul con manchas moradas te tiene compasión, derrumba a los otros monstruos y te da a escoger dos posibles rutas de escape. A tu izquierda ves una puerta de metal muy gruesa, a tu derecha una puerta de madera convencional. Elige rápido que la araña gigante viene corriendo acompañada de un Pejelagarto.\n\nA.Metal\nB.Madera")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      metal(eleccion,contador)
      a = True 
    if eleccion == "B" or eleccion == "b":
      madera(eleccion,contador)
      a = True

def madera(eleccion,contador):
  print ("\nEntras en lo que parece ser la habitación de una niña pequeña, cuando intentas salir de la habitación la niña grita desesperada y sus padres vienen corriendo, cuando te ven te golpean con un bate de béisbol y te noquean cuando abres los ojos hay ocho policías rodeándote y te llevan a la cárcel, mientras esperan el juicio, el día de juicio el Juez decide condenarte a cadena perpetua por tentativa de acceso carnal violento a una menor de 14 años\n\nAmárrate el jabón a la mano cuando te bañes en la cárcel.\n")
  contador[22]+=1 
 
def metal(eleccion,contador):
  b = False
  while b == False:
    print("\nCuando el oso de colores pastel te arroja por la puerta puedes sentir mucho frio recorrer tu cuerpo, y escuchas una voz amigable decir: “BIENVENIDO AL HIMALAYA” cuando alzas la mirada es una figura humana extremadamente grande y cubierta en pelo blanco. Te cuenta la historia de como fue desterrado de mostruopolis, una ciudad cuyo nombre nunca habías escuchado, después de dice que hay una villa muy cerca, pero antes de que digas cualquier otra cosa, te ofrece un helado de limón de dudosa apariencia\n\nA.Aceptar el helado\nB.Ir a la villa")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      ahelado(eleccion,contador)
      b = True
    if eleccion == "B" or eleccion == "b":
      villa0(eleccion,contador)
      b= True
def ahelado(eleccion,contador):
  c = False
  while c == False:
    print("\nCuando le vas a pegar el primer mordisco al helado escuchas una voz muy aguda salir de el, y te das cuenta que el helado está vivo, pegas un grito y el monstruo del Himalaya te lo cambia, este si parece estar bueno.\n\nA.Comer el helado\nB.Tirar el helado")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      print ("\nEl helado estaba bueno :D, luego se dirigen a la villa")
      villa1(eleccion,contador)
      c = True
    if eleccion == "B" or eleccion == "b":
      print("\nLo tiras como si fuera una bola de nieve. El monstruo no se da cuenta, solo observa que ya tienes tu cono vacío. Luego se dirigen a la villa, pero justo antes de salir de la caverna en la que se encuentran te resbalas con el helado que estaba en el piso.")
      villa0(eleccion,contador)
      c = True
def villa0(eleccion,contador):
  print("\nBajas y te das cuenta que estás en un lugar muy parecido a Nepal, una pandilla de Monstruos con cachetes colorados te secuestra, y te obligan a ser su esclavo y criar cabras toda la vida\n\nEse helado no era tan mala idea después de todo...\n")
  contador[23]+=1 

def villa1(eleccion,contador):
  print("\nBajas y te das cuenta que estás en un lugar muy parecido a Nepal, una pandilla de Monstruos con cachetes colorados te secuestra, y te obligan a ser su esclavo y criar cabras toda la vida\n\nEy pero el helado estaba bueno.\n")
  contador[24]+=1 


def mundodepiedra(eleccion,contador):
  d = False
  while d == False:
    print("\nEs 3 de Abril en la Madrugada ¿Eres la padre, la madre o el hijo?\n\nA.Padre\nB.Madre\nC.Hijo")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      print ("\nSon las 2 de la mañana")
      time.sleep(2)
      print ("Tienes un hijo que amas y una esposa que finges querer ")
      time.sleep(2)
      print ("Debes patrullar de noche toda la semana")
      time.sleep(2)
      print ("Te vistes y te vas en tu patrulla policíaca a lucir tu placa y enjuiciar a todo el que pasa")
      time.sleep(2)
      print ("Una hora pasa y consigues juntar una paca de dinero que seguramente gastarás con fufas en la taberna")
      time.sleep(2)
      print ("Se hacen las tres y cuarto")
      time.sleep(2)
      print ("Aceleras el paso")
      time.sleep(2)
      print ("Pasas por una esquina y escuchas a un muchacho gritando")
      time.sleep(2)
      print ("Lo estaban asaltando, solo echas un corto vistazo")
      time.sleep(2)
      print ("Sin embargo, no haces caso y sigues manejando")
      time.sleep(2)
      print ("Rumbo al burdel de siempre te dirigías")
      time.sleep(2)
      print ("Y mientras conducías, notas que un taxi, de cerca te seguía.“Han de ser vainas mías” dices mientras sonríes")
      time.sleep(2)
      print ("Y al llegar pagas por la mejor prostituta que había, una rubia de infarto")
      time.sleep(2)
      print ("La metes para el cuarto")
      time.sleep(2)
      print ("Entre sus piernas pruebas el tacto y comienzas el acto")
      time.sleep(2)
      print ("Pero en menos de un minuto escuchas unos pasos entrar")
      time.sleep(2)
      print ("Y PUM mueres ipso facto.")
      time.sleep(2)
      contexto(i)
      contador[25]+=1 
      d = True
    if eleccion == "B" or eleccion == "b":
      print ("\n15 para las 2 de la mañana")
      time.sleep(2)
      print ("Te levantas para atender a tu esposo Carlos")
      time.sleep(2)
      print ("Le preparas algo de comer y dejas su ropa planchada")
      time.sleep(2)
      print ("Media hora después él se va;luego de un beso sin ganas comienza el drama")
      time.sleep(2)
      print ("Sales muy rápido de tu casa ")
      time.sleep(2)
      print ("“Siga despacio a esa patrulla”, le dices al taxista")
      time.sleep(2)
      print ("Una hora estuvieron buscando a Carlos con sigilo")
      time.sleep(2)
      print ("Luego lograron seguirlo con dirección hacia un prostíbulo")
      time.sleep(2)
      print ("Acto seguido suena tu teléfono, era tu hijo al que le dices “ahora no puedo” y le cuelgas")
      time.sleep(2)
      print ("No puedes hablar por la ira de saber lo que verías")
      time.sleep(2)
      print ("Llegas, entras y preguntas por Carlos, el policía")
      time.sleep(2)
      print ("Pagas lo que tenías por la llave que abrirá el cerrojo")
      time.sleep(2)
      print ("Para entrar dices que te unirás en una orgía con tu esposo")
      time.sleep(2)
      print ("Abres y de inmediato, cegada por el enojo del bolso sacas un arma y PUM a Carlos entre sus ojos.")
      time.sleep(2)
      contexto(i)
      contador[26]+=1 
      d= True
    if eleccion == "C" or eleccion == "c":
      print ("\n2:30 de la mañana")
      time.sleep(2)
      print ("En tu almohada escondes la marihuana que fumas siempre")
      time.sleep(2)
      print ("Te das cuenta de que en casa no hay gente")
      time.sleep(2)
      print ("Así que llamas al que te vende y cuadras un trueque, a las tres y cuarto en la esquina han de verse para abastecerse")
      time.sleep(2)
      print ("Llegas puntualmente y de repente sientes un cañón en tu frente del jíbaro que una trampa te tiende")
      time.sleep(2)
      print ("Te dice, dame la cartera, el reloj y las prendas")
      time.sleep(2)
      print ("Cuando ves que pasa una patrulla en plena contienda, era tu padre que sigue de largo")
      time.sleep(2)
      print ("Mientras el jíbaro te suelta disparos al pecho y a la pierna")
      time.sleep(2)
      print ("Solamente el teléfono logras esconder y llamas a tu madre para que te vaya a socorrer")
      time.sleep(2)
      print ("Pero al atender, fue lo último que escuchaste")
      time.sleep(2)
      print ("La voz de ella diciendo “no puedo” y te colgó")
      time.sleep(2)
      contexto(i)
      contador[27]+=1
      d= True
  
def contexto(i):
  print("\nUn funcionario de la Policía Nacional\nIdentificado como Carlos Camacaro de 46 años de edad\nFue asesinado por su esposa, la ciudadana María Hernández de Camacaro\nEn un reconocido local nocturno de la ciudad de Bogotá\nLa mujer, de 43 años de edad, se encuentra a la orden de la Fiscalía\nEn otras noticias, un joven de 17 años\nFue hallado sin vida esta madrugada en el 20 de Julio\nEl joven fue encontrado sin sus pertenencias.")
  print("\nEstamos viviendo en un mundo de Piedra.\n")


def telafumasteperoverde(eleccion,contador):
  a=False
  while a == False:
    print("\nApareces en la pendiente de una colina, al frente tuyo ves una cápsula metálica cilíndrica que está enterrada a lo lejos, puedes ir o quedarte acá parado.\n\nA.Ir\nB.Quedarte donde estás")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      capsula(eleccion,contador)
      a=True
    elif eleccion == "B" or eleccion == "b":
      print ("\nRepentinamente escuchas un rugir del cielo. No alcanzas a reaccionar cuando un meteorito cae y te aplasta en el lugar.\n\nXD, lo siento pero de algo tenías que morir.")
      print(" ")
      contador[28]+=1
      a=True
def imprime(matriz):
 for i in range(len(matriz)):
        print(*matriz[i],sep="  ",end="")
        print()

def capsula(eleccion,contador):
  e = False
  while e == False:
    print("\nAl llegar al lugar puedes observar lo que parece ser la ropa de una persona tal como si hubiera desaparecido y sus prendas simplemente cayeron al suelo. Respiras profundamente, tragas saliva y decides indagar que hay en la cápsula. Al querer entrar en ella te das cuenta de que no está hecha de un metal común, tiene unas marcas en forma de fractal en toda su estructura. Luego de unos segundos escuchas ruidos provenientes del interior de la cápsula y encuentras lo que parece ser un panel para abrir el compartimento superior de la cosa.\n\nA.Acercarte al panel\nB.Ignorar el panel")
    eleccion=input()
    if eleccion == "A" or eleccion == "a":
      e = True
      print("\nTe acercas y te das cuenta que es un panel numérico, segurmanete es para ingresar alguna contraseña...\n")
      imprime([[1,2,3],[4,5,6],[7,8,9],[' ',0,' ']])
      contrasena=input('PIN: ')
      i=0
      z=False
      while i<3:
        if contrasena != str(8054):
          i+=1
          print("\nNo pasa nada, seguro no es la contraseña correcta")
          contrasena=input('PIN: ')
        if contrasena == str(8054):
          print("\nTe das cuenta de que los sonidos se intensifican, te alejas de allí despacio. En ese momento se abre una compuerta de la cual sale un ser que parece ser de otro planeta. Tiene una cabeza humana suspendida sobre 12 tentáculos, su rostro a pesar de ser antropomorfo tiene características peculiares como dientes supremamente afilados y ojos de lagarto.")
          time.sleep(1.5)
          print("Al mirarlo directamente a los ojos quedas envuelto en una ilusión. Empiezas a tomar forma de todas las especies conocidas por el humano, e incluso todas las que no…..")
          time.sleep(1.5)
          print("Despiertas y te encuentras en un lugar oscuro, donde te torturan con todos los malos recuerdos que has vivido hasta ese momento. Tu cerebro no soporta el dolor y entras en un estado de locura perpetua...")
          print(" ")
          print("No se sabe que es peor, la realidad o esta pesadilla")
          print(" ")
          contador[30]+=1
          z=True
          i=4
      if z == False:
        print ("\nAparece un laser que te está apuntando directamente a la frente. Intentas correr, pero ya es tarde, acabas de ser desintegrado")
        print(" ")
        print("Mirar y no tocar se llama respetar")
        print(" ")
        contador[29]+=1
    
    if eleccion == "B" or eleccion == "b":
      print("\nTe das cuenta de que los sonidos se intensifican, te alejas de allí despacio. En ese momento se abre una compuerta de la cual sale un ser que parece ser de otro planeta. Tiene una cabeza humana suspendida sobre 12 tentáculos, su rostro a pesar de ser antropomorfo tiene características peculiares como dientes supremamente afilados y ojos de lagarto.")
      time.sleep(1.5)
      print("Al mirarlo directamente a los ojos quedas envuelto en una ilusión. Empiezas a tomar forma de todas las especies conocidas por el humano, e incluso todas las que no…..")
      time.sleep(1.5)
      print("Despiertas y te encuentras en un lugar oscuro, donde te torturan con todos los malos recuerdos que has vivido hasta ese momento. Tu cerebro no soporta el dolor y entras en un estado de locura perpetua...")
      print("\nNo se sabe que es peor, la realidad o esta pesadilla\n")
      contador[30]+=1
      e = True
    
def ruben0(eleccion,contador):
  print ("\nEstás borracho y por alguna razón estás convencido")
  time.sleep(2)
  print ("Que el alcohol no te afecta los sentidos")
  time.sleep(2)
  print ("Por el contrario que tus reflejos son mucho más claros y tienes más control")
  time.sleep(2)
  print ("Por eso hundes el pie en el acelerador")
  time.sleep(2)
  print ("Subes el volumen de la radio para sentirte mejor, bien chévere")
  time.sleep(2)
  print ("Y cuando la luz cambia a amarilla")
  time.sleep(2)
  print ("Las ruedas del carro chilla")
  time.sleep(2)
  print ("Y te crees un James Bond")
  time.sleep(2)
  print ("Decides la luz del semáforo comerte")
  time.sleep(2)
  print ("Y no ves el camión aparecerse en la oscuridad")
  print(" ")
  time.sleep(2)
  print("Pito, choque y la pregunta ¿Qué pashó? para la eternidad")
  print(" ")
  contador[31]+=1


def ruben1(eleccion,contador):
  print ("\nEres un señor que vive en una casa de alquiler")
  time.sleep(2)
  print ("Y a pesar de que ya tienes mujer")
  time.sleep(2)
  print ("Has decidido tener una aventura a lo casanova")
  time.sleep(2)
  print ("Y le has propuesto a una vecina, que es casada")
  time.sleep(2)
  print ("De la manera más vulgar y descarada ")
  time.sleep(2)
  print ("Que, cuando su marido al trabajo se haya ido, te llame")
  time.sleep(2)
  print ("Para ser su enamorado")
  time.sleep(2)
  print ("La señora, que no es boba, se lo cuenta a su marido")
  time.sleep(2)
  print ("Y el tipo decide invitar al atrevido")
  time.sleep(2)
  print ("Y ella te cita cual lo acordado")
  time.sleep(2)
  print ("Y sales todo perfumado con ropa limpia que tu esposa te ha planchado")
  time.sleep(2)
  print ("Y traes una flor que te encontraste en el tendedero")
  time.sleep(2)
  print ("Y en casa de la vecina está el marido")
  time.sleep(2)
  print ("Indeciso sobre dónde te va a dar primero con un bate de béisbol del extranjero")
  time.sleep(2)
  print ("Suena el timbre, ring-ring y no es el Gran Combo")
  time.sleep(2)
  print("Comienza la segunda del noveno")
  time.sleep(2)
  print(" ")
  print("Decisiones, cada día, alguien pierde, alguien gana, Ave María")
  print(" ")
  contador[32]+=1
 
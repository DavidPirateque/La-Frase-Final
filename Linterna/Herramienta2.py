#Linterna
i = 0  
def linterna(n,contador):
  print("\nEmpiezas a sentir mucho frio, abres la puerta y divisas un desierto de nieve donde no alcanzas a ver nada a lo lejos, con ayuda de la linterna te vas guiando hasta que encuentras una tienda de campaña que parece estar rasgada.")
  I0=False
  while I0 == False:
    print("\nSolo puedes escoger uno ¿Cuál eliges? \nA: Entrar a ver que hay dentro \nB: Dar una vuelta alrededor")
    I = input()
    if I == "A" or I == "a":
      I0=True
      N0=False
      while N0== False:
        print("\nCuando entras ves un par de cadáveres que parece que fueron atacados por una bestia y un pequeño niño de brazos que llora desconsolado, a su lado ves una maleta con elementos de supervivencia, pero te das cuenta que solo puedes cargar uno ¿Qué llevas?")
        print("\nSolo puedes escoger uno ¿Cuál eliges? \nA: Bebe \nB: Maleta")
        N = input()
        if N == "A" or N == "a" : 
          N0=True
          H0=False
          while H0==False:
            print("\nAntes de salir de la tienda tomas una cinta dentro de la maleta con la cual te pegas la linterna a la cabeza, empiezas a caminar con el bebe en brazos y pasadas unas horas de no encontrar refugio, la linterna empieza a alumbrar intermitentemente, por lo cual tienes que acelerar el paso, a su vez escuchas pasos sobre la nieve")
            print("\nSolo puedes escoger uno ¿Cuál eliges? \nA: Correr \nB: Esperar teniendo fe de que sea una persona")
            H=input()
            if H == "A" or H == "a":
              H0=True
              J0=False
              while J0 == False:
                print("\nSolo puedes escoger uno ¿Cuál eliges? \nA: Derecha \nB: Izquierda")
                J= input()
                if J == "A" or J=="a":
                  J0=True
                  M0=False
                  while M0 == False:
                    print("\nCreíste escuchar al oso detrás de ti, pero en realidad estaba a tu derecha, tienes dos opciones")
                    print("\nSolo puedes escoger uno ¿Cuál eliges? \nA: Morir junto al bebe \nB: Tirar al bebe como una carnada y correr")   
                    M=input()
                    if M=="A" or M=="a":
                      M0=True
                      print("\nAunque sabes que la muerte es inminente tratas de luchar con el oso, el animal te gana, aplastando tus piernas, mientras te retuerces de dolor ves como el oso se come al bebe para proseguir a comerte a ti\nLos caminos de la vida no son como tu esperabas.\n") 
                      contador[8]+=1
                      
                    elif M=="B" or M=="b":
                      M0=True
                      print("\nTras arrojar el bebe a las garras del oso, corres sin mirar atrás para evitar remordimiento, sigues corriendo a lo largo de unos minutos mientras oyes que los pasos del oso te siguen persiguiendo, al fin se te acaba la batería de la linterna y corres sin saber a donde vas terminas cayendo por un risco de 100 metros de altura\nTiraste al bebe como alimento para el oso y terminaste como alimento para los peces.\n")
                      contador[9]+=1

                elif J=="B" or J=="b":
                  J0=True
                  U0=False
                  while U0 == False:
                    print("\nLogras escapar del oso, y sigues corriendo hasta que encuentras una cueva donde ves lo que parece ser un militar refugiándose junto a una fogata. Te acercas a la cueva y al verte con el bebe el militar se sorprende ya que el es el guarda espaldas de la familia que te encontraste previamente. Mientras le cuentas lo que pasó escuchan el oso acercarse tienes dos opciones\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Utilizar el arma del guardaespaldas \nB: Usar la fogata")
                    U=input()
                    if U == "A" or U == "a":
                      U0=True
                      C0=False
                      while C0== False:
                        print("\nSe dan cuenta que ya solo le queda una bala. En medio de la angustia, le quitas el arma al guardaespaldas y disparas, como no tienes experiencia impactas mal y el oso no muere. Buscas con que defenderte\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: El arma ya sin balas \nB: La fogata")
                        C=input()
                        if C =="A" or C==("a"):
                          C0=True
                          print("\nUtilizas el arma para golpear al oso, lo que hace que se ponga más furioso. Este se para y se los come a todos\nCreo que esta muerte no necesita frase irónica porque ya es suficientemente estúpido intentar matar un oso de un cachazo.\n")
                          contador[10]+=1
                        elif C == "B" or C == "b":
                          C0=True
                          print("\nEl fuego asusta al oso por lo que se va de la cueva, aunque el militar ya se ha intentado comunicar con la base por medio de un radio que porta, esperan al otro día para seguir intentando, por fin contestan y vienen a salvarlos. Los familiares demuestran su gratitud por salvar al niño ayudándote económicamente por el resto de tu vida\nRecuerda que esto es un juego porque en la vida real nunca te pasaría, jaja =').\n") 
                          contador[11]+=1
                    elif U == "B" or U == "b":
                      U0=True
                      print("\nEl fuego asusta al oso por lo cual no se acerca a la cueva, aunque el militar ya se ha intentado comunicar con la base por medio de un radio que porta. Esperan al otro día para seguir intentando, por fin contestan y vienen a salvarlos. Los familiares demuestran su gratitud por salvar al niño ayudándote económicamente por el resto de tu vida \nRecuerda que esto es un juego porque en la vida real nunca te pasaría, jaja =').\n") 
                      contador[11]+=1
                    
            elif H=="B" or H=="b":   
              H0=True
              print("\nEntre la intermitencia de la linterna ves muy poco, pero cuando ya es muy tarde ves que era el oso que se acercaba a ustedes, el oso se tira sobre ti, aplastando al bebe y comiéndote lentamente. Antes de morir se te viene a la cabeza el número 8054, sabrá Dios por qué será....\nNo todos los abrazos de osos son cariñosos.\n") 
              contador[12]+=1   
        elif N == "B" or N == "b":  
          N0=True
          W0=False
          while W0 == False:
            print("\nSales de la tienda procurando no mirar atrás, sigues caminando para encontrar un lugar en el que te puedas refugiar del animal que está al acecho, tu linterna empieza a parpadear por la falta de batería, buscas en la maleta y encuentras pilas de repuesto, cuando te agachas a colocar la pila en la linterna escuchas pasos en la nieve\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Correr \nB: Esperar teniendo fe de que sea una persona")
            W=input()
            if W == "a" or W =="A":
              W0 = True
              K0=False
              while K0==False:
                print("\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Izquierda \nB: Derecha")
                K=input()
                if K == "A" or K =="a":
                  K0=True
                  print("\nLogras escapar del oso, pero luego de 3-4 horas de caminar sin rumbo fijo el frio empieza a congelar tus extremidades, buscas en la maleta algo que te pueda dar calor, sin embargo nada de lo que hay dentro es útil, al pasar el tiempo mueres de hipotermia\nTal vez el calor del bebe te hubiera salvado, nunca lo sabremos... o ¿si?.\n")
                  contador[13]+=1 
                  
                elif K =="B" or K =="b":
                  K0=True
                  Y0=False
                  while Y0==False: 
                    print("\nDespués de correr un tiempo encuentras algo que parece ser una cueva conde ves todavía el humo de una especie de fogata en ella. Te acercas sin saber que esperar y encuentras un cadáver irreconocible lleno de mordidas y rasguños, se nota que no hace murió ya que la sangre está fresca y la leña sigue caliente. Al lado del cadáver ves un arma que no tiene municiones.\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Buscar en la ropa del cadaver \nB: Buscar al rededor de la cueva")
                    Y=input()
                    if Y =="A" or Y == "a" :
                      Y0=True
                      G0=False
                      while G0==False:
                        print("\nMientras buscas escuchas el oso acercarse pero logras encontrar una bala llena de sangre\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Secar la bala \nB: Utilizarla así")
                        G=input()
                        if G == "A" or G =="a":
                          G0=True
                          V0=False
                          while V0==False:
                            print("\nLogras poner la bala en su lugar e impactar en el cráneo del oso, ya estás muy cansado y te acuestas junto al oso ya sin vida. Al amanecer tienes mas visibilidad y ves un radio, te comunicas con una persona que dice ser el jefe de seguridad de la familia mas adinerada de Alaska, y mandan un helicóptero por ti, cuando llegan ven a tu lado el cuerpo del guardaespaldas principal de esta familia, te preguntan por lo que sucedió al explicarles preguntan por el bebe\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Mientes \nB: Dices la verdad")
                            V=input()
                            if V == "A" or V=="a":
                              V0=True
                              print("\nTe llevan con ellos y te ayudan en todo, hasta te dan un apoyo económico vitalicio por lo sucedido, pero el remordimiento de ganar este dinero por haber dejado un niño morir en el frio te lleva al suicidio \n¿Quién diría que no pudiste vivir con tus decisiones?\n") 
                              contador[14]+=1 
                            
                            elif V=="B" or V=="b":
                              V0=True
                              print("\nAl escuchar todo lo ocurrido, estas personas que le tenían mucho cariño a esta familia, mas que todo al bebe, deciden desnudarte y dejarte en el frio, hasta que mueres por hipotermia \nTodo se paga con la misma moneda.\n")
                              contador[15]+=1 
                            
                        elif G =="B" or G =="b":
                          G0=True
                          print("\nPones la bala en su lugar y cuando apuntas y disparas el arma no funciona y solo sientes una garra destrozando tu cuello \n¿Cómo se te ocurre usar una bala mojada?\n")
                          contador[16]+=1 
                        
                    elif Y == "B" or Y =="b":
                      Y0=True
                      print("\nMientras buscas municiones se acerca el oso y salta sobre ti, tratas de controlarlo con tus manos, pero es inútil \nDebiste ser mas rápido.\n")
                      contador[17]+=1 
            elif W == "B" or W =="b":
              W0=True  
              print("\nCuando logras poner la pila y encender la linterna ya es muy tarde solo alcanzas a ver las amígdalas del oso y sus colmillos rodeando tu campo de visión\nEs iluso en esta vida creer en los milagros, mas aun cuando te negaste a ser parte de uno.\n")
              contador[18]+=1 
    elif I == "B" or I == "b":
      I0=True
      S0=False
      while S0==False:
        print("\nVes las pisadas de algo que parece un oso, ya que comparas tus pies junto a la huellas y no es ni la mitad del tamaño. Escuchas ruidos provenientes de lo que queda de la tienda y te acercas a observar. Ves las sombras de dos cuerpos inertes y un pequeño objeto que se mueve\n\nSolo puedes escoger uno ¿Cuál eliges? \nA: Entrar a ver que hay dentro \nB: No darle importancia y continuar.")
        S=input()
        if S =="A" or S =="a":
          S0=True
          print("\nTe acercas, pero cuando notas el tamaño de lo que está moviéndose adentro empiezas a correr, sin embargo escuchas pasos detrás de ti. No quieres voltear, pero cuando lo haces ya es muy tarde. Lo último que alcanzas a ver es como un animal te devora lentamente en la penumbra del Ártico\nLa curiosidad mató al gato.\n")
          contador[19]+=1 
          
        elif S == "B" or S == "b":
          S0=True
          print("\nDecides seguir por tu camino pero después de unos minutos escuchas unos pasos tras de ti, decides ignorarlos y volteas cuando ya es muy tarde, lo último que alcanzas a ver es como un animal te devora lentamente en la penumbra del Ártico \nTal vez la curiosidad hubiera salvado al gato.\n")
          contador[20]+=1 
       
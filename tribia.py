while True:
    print ("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIA\n")
    print("1)-ingrese Ficha del paciente\n")
    print("2)-Buscar ficha por rut\n")
    3)-Buscar medicamentos por rut\n4)-Eliminar ficha del paciente\n5)-Lista de pacientes atendidos\n6)-Salir"

    def opcion1():
        while True:
            for x in i:
                da=input(f"{x}:\n ")
                datos.append(da)
            rt=(datos[2])
            a=len(datos[2])
            b=len(datos[5])
            if (a==9 or a==8):
                if (b==9 or b==8):
                    dia=input("Diagnostico:\n ")
                    diagnostico.append(dia)
                    med=input("Medicamento:\n ")
                    medicamento.append(med)
                    rut.append(rt)
                    break
            else:
                print("El Rut o el Telefono ingresados son invalidos. ")
                continue
    def opcion2():
        print("2")
    def opcion3():
        print("3")
    def opcion4():
        print("4")
    def opcion5():
        print("5")
    datos=[]
    diagnostico=[]
    medicamento=[]
    rut=[]
    i=["Nombre","Apellido","Rut","Estado civil","Domicilio","Fono"]
    print ("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIA\n\n1)-ingrese Ficha del paciente\n2)-Buscar ficha por rut\n3)-Buscar medicamentos por rut\n4)-Eliminar ficha del paciente\n5)-Lista de pacientes atendidos\n6)-Salir")
    op=int(input("Ingrese una opcion: "))
    if op==1:
        opcion1()
        continue
    elif op==2:
        opcion2()
        continue
    elif op==3:
        opcion3()
        continue
    elif op==4:
        opcion4()
        continue
    elif op==5:
        opcion5()
        continue
    elif op==6:
        break
    else:
        print("Opcion invalida vuelva a escoger ")
        continue
    break


import random
import time
iniciar_trivia = True
intentos = 0
while iniciar_trivia == True:
    intentos = 1
    puntaje = 0
    puntaje = random.randint(0,5)
    print("bienvenidos a mi trivia sobre computacion")
    print("pondremos a prueba tus conocimientos")
    print("tienes", puntaje, "puntos")
    nombre = input("ingresa tu nombre y presiona 'enter'   cuando estes listo")
    print("\n hola", nombre, "responde las preguntas   escribiendo la letra de la alternativa y presionando  'enter' para enviar tu respuesta")
   #pregunta 1
    print("1) ¿quien fue el creador de windows?")
    print("a) Elon Musk")
    time.sleep(1)
    print("b) Linus Torvalds")
    time.sleep(1)
    print("c) Bill Gates")
    time.sleep(1)
    print("d) Mark Zuckerberg")
    time.sleep(1)
    respuesta_1 = input("\ntu respuesta: ")
    while respuesta_1 not in ("a", "b", "c", "d"):   
        respuesta_1 = input("debes responder a, b, c o d.  ingresa     nuevamente tu respuesta: ")
        if respuesta_1 == "c":
           puntaje += 10
           print("excelente", nombre, "ganaste 10 puntos")
        else:
           print("incorrecto", nombre,)
    #pregunta 2
    print("2) ¿cual es el lenguaje de programacion mas facil   de   aprender")
    print("a) python")
    time.sleep(1)
    print("b) PHP")
    time.sleep(1)
    print("c) C")
    time.sleep(1)
    print("d) javascript")
    time.sleep(1)
    respuesta_2 = input("\ntu respuesta: ")
    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input("debes responder a, b, c o d.   ingresa   nuevamente tu respuesta: ")
        if respuesta_2 == "b":
          print("incorrecto", nombre, "PHP es un lenguaje de alto   nivel")
        elif respuesta_2 == "c":
          print("incorrecto", nombre, "C es un lenguaje de alto   nivel")
        elif respuesta_2 == "d":
          print("incorrecto", nombre, "javascript es un lenguaje   de alto  nivel")
        else:
          puntaje += 10
          print("excelente", nombre, "tienes 10 puntos")
    #pregunta 3
    print("3) ¿quien fue el creador de paypal?")
    print("a) Jeff Bezos")
    time.sleep(1)
    print("b) Yu Pan")
    time.sleep(1)
    print("c) Nigel Morris")
    time.sleep(1)
    print("d) Reed Hastings")
    time.sleep(1)
    respuesta_3 = input("\ntu respuesta: ")
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input("debes responder a, b, c o d.  ingresa nuevamente tu respuesta")
    if respuesta_3 == "b":
      puntaje += 10
      print("excelente", nombre, "tienes 10 puntos")
    else:
      print("incorrecto", nombre,)
  #pregunta 4
    print("4) ¿que lenguaje de programacion solo se puede  utilizar en  los softwares de apple? ")
    print("a) C")
    time.sleep(1)
    print("b) python") 
    time.sleep(1)
    print("c) java")
    time.sleep(1)
    print("d) swift") 
    time.sleep(1)
    respuesta_4 = input("\ntu respuesta: ")
    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input("debes responder a, b, c o d.  ingresa nuevamente tu respuesta")
        if respuesta_4 == "a":
          print("incorrecto", nombre, " C es un lenguaje  universal")
        elif respuesta_4 == "b":
          print("incorrecto", nombre, " Python es un lenguaje   universal")
        elif respuesta_4 == "c":
          print("incorrecto", nombre, "Java es un lenguaje   universal")
        else:
          puntaje += 10
          print("excelente", nombre, "tienes 10 puntos")
    print("gracias", nombre, "por jugar mi trivia,   alcanzaste", puntaje, "puntos")
    print("\n¿Deseas intentar la trivia nuevamente?") 
    repetir_trivia = input("Ingresa 'si' para repetir, o   cualquier tecla para finalizar: ").lower()
    if repetir_trivia != "si":
      print(f"\nEspero {nombre} que lo hayas pasado bien,   hasta pronto!")
      iniciar_trivia = False
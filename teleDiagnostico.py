#VERSION BY: WEMBIE

#Developed by:

#Wembie.

def opciones():
  print("\n0 -> Nunca")
  print("1 -> Varios dias")
  print("2 -> Mas de la mitad de los dias")
  print("3 -> Casi cada dia")

def tablaResultados(resultado, nombre):
  print(f"\n-> RESULTADOS: {resultado} <-\n")
  print("Menor a 13 -> No eres depresivo")
  print("Menor a 26 -> Eres un poco depresivo")
  print("Menor a 39 -> Eres medianamente depresivo")
  print("Mayor a 39 -> Eres depresivo\n")
  if resultado <= 13:
    print(f"{nombre} no eres depresivo")
    #Le aumentan mas cosas.. nose q mas equisde
  if resultado <= 26 and resultado >= 13 :
    print(f"{nombre} eres un poco depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x2
  if resultado <= 39 and resultado >= 26 :
    print(f"{nombre} eres medianamente depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x3
  if resultado > 39:
    print(f"{nombre} eres depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x4
    
def teleDiagnostico():
  print("TEST PARA DEPRESION\n")
  nombre = input("Digita tu nombre: ")
  preguntas = ["Poco interés o alegría por hacer cosas",
               "Sensación de estar decaído/a, deprimido/a o desesperanzado/a",
               "Problemas para quedarse dormido/a, seguir durmiendo o dormir demasiado",
               "Sensación de cansancio o de tener poca energía",
               "Poco apetito o comer demasiado",
               "Sentirse mal consigo mismo/a; sentir que es un/a fracasado/a; o que ha decepcionado a su familia o a sí mismo/a",
               "Problemas para concentrarse en algo, como leer el periódico o ver televisión",
               "Moverse o hablar tan despacio que los demás pueden haberlo notado. O lo contrario, estar tan inquieto/a o agitado/a que se ha estado moviendo de un lado a otro más de lo habitual",
               "Pensamientos de que estaría mejor muerto/a o de querer hacerse daño de algún modo"]
  inicio = 0
  resultado = 0 #Mayor posible -> 54
  while inicio <= 8:
    print(f"\nPregunta {inicio + 1}: {preguntas[inicio]}")
    opcionPregunta = None
    opciones()
    while True:
      opcionPregunta = int(input("\nDigite el numero deseado: "))
      if opcionPregunta <= 3 and opcionPregunta >= 0:
        if opcionPregunta == 0: #NUNCA
          resultado += 0
        if opcionPregunta == 1: #VARIOS DIAS
          resultado += 1
        if opcionPregunta == 2: #MAS DE LA MITAD DE LOS DIAS
          resultado += 3
        if opcionPregunta == 3: #CASI CADA DIA
          resultado += 6
        break
      else:
        print("\nNumero invalido, porfavor digitalo nuevamente.")
    inicio += 1
  tablaResultados(resultado, nombre)
teleDiagnostico() 

##############################################

#VERSION BY: JUAN JOSE RESTREPO

banco_preguntas = [
    "1.Poco interés o alegría por hacer cosas", "2.Sensación de estar decaído/a, deprimido/a o desesperanzado","3.Problemas para quedarse dormido, seguir durmiendo o dormir demasiado","4.Sensación de cansancio o de tener poca energía","5.Poco apetito o comer demasiado","6.Sentirse mal consigo mismo; sentir que es un/a fracasado; o que ha decepcionado a su familia o a sí mismo", "7.Problemas para concentrarse en algo, como leer el periódico o ver televisión", "8.Moverse o hablar tan despacio que los demás pueden haberlo notado. O lo contrario, estar tan inquieto/a o agitado/a que se ha estado moviendo de un lado a otro más de lo habitual", "9.Pensamientos de que estaría mejor muerto/a o de querer hacerse daño de algún modo"
]

def preguntas(preguntas):
    total_preguntas = len(preguntas)
    contador = 0
    contadorSi = 0
    contadorNO = 0
    while contador < total_preguntas:
        for i in preguntas:
            opcion = input(f"\n{i} [Si/No]: ")
            if opcion.lower() == "si":
                contadorSi += 1
            elif opcion.lower() == "no":
                contadorNO += 1
            else:
                print("\nCaracter invalido")
                print("Por favor digitelo nuevamente")
            contador += 1
    return contadorSi, contadorNO

def diagnostico(resultado):
    
    porcentaje = round(((resultado*100)/9), 2 )
    if resultado > 6:
        print("Presenta sintomas graves. Recomendamos la atencion de un profesional urgentemente. Tienes un {} %".format(porcentaje) + " de depresion")
    elif resultado < 6 and resultado >= 4:
        print("Presentas sintomas medios de depresion. Tienes un {} %".format(porcentaje) + " de depresion") 
    elif resultado < 4 and resultado >= 2:
        print("Presentas sintomas de leves depresion. Tienes un {} %".format(porcentaje) + " de depresion")
    else:
        print("Tus sintomas no son graves. Tienes un {}%".format(porcentaje) + " de depresion")

resultado1, resultado2 = preguntas(banco_preguntas)

print("Si: ", resultado1)
print("No: ", resultado2)
diagnostico(resultado1)

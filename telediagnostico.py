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
    porcentaje = 0
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
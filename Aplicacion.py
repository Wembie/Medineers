print("Hola Wembie")
def menu():
  print("1. Registrar.")
  print("2. Buscar paciente")
  print("3. Borrar paciente")
  print("4. Ver total pacientes.")
  print("0. Salir.")
opcion = -1
while opcion != 0:
  while True:
    try:
      opcion = int(input("Digite el numero deseado [0,1,2,3,4]: "))
    except ValueError:
      print("Solo se recibe numeros enteros")
    else:
      break

#Developed by:

#Wembie.
#Juan Jose Restrepo.
#Daniela Gomez.
#Jose Miguel Lopez.


import marshal
import os.path as path
from os import remove

def bienvenida():
  print("—————— SOFTWARE BY MEDINEERS ——————")
  print("")
  print("——————————— Bienvenid@ ————————————")
  print("——————————————— a —————————————————")
  print("——————————— Psycho 19 —————————————")
  
def menu():
  print("\n1. Registrar paciente")
  print("2. Buscar paciente")
  print("3. Borrar paciente")
  print("4. Ver total pacientes")
  print("5. Borrar datos")
  print("0. Salir.")
  
opcion = None
pacientes = []
if path.exists("pacientes"):
  archivo = open("pacientes","br")
  pacientes = marshal.load(archivo)
  archivo.close()
else:
  archivo = open("pacientes","bw")
  marshal.dump(pacientes,archivo)
  archivo.close()
bienvenida()
while opcion != 0:
  menu()
  while True:
    try:
      opcion = int(input("\nDigite el numero deseado [0,1,2,3,4,5]: "))
      print("")
    except ValueError:
      print("\nSolo se recibe numeros enteros")
    else:
      if opcion >=0 and opcion <= 5:
        break
      else:
        print("Numero invalido")
        print("Por favor digitelo nuevamente")
  if opcion == 1:
    paciente = []
    nombreCompleto = input("Digite su nombre completo: ")
    cedula = None
    encontroCedula = None
    while True:
      try:
        cedula = int(input("Digite su cedula: "))
      except ValueError:
        print("\nSolo se recibe numeros enteros")
      else:
        for i in range(len(pacientes)):
          if pacientes[i][0] == cedula:
            print(f"La cedula {cedula} ya esta registrada")
            encontroCedula = 1
            break
        if encontroCedula is None:
          break
    print(f"\nEl paciente {nombreCompleto}")
    print("Ha sido registrado con exito!")
    paciente.append(cedula)
    paciente.append(nombreCompleto)
    pacientes.append(paciente)
    archivo = open("pacientes","bw")
    marshal.dump(pacientes,archivo)
    archivo.close()
  if opcion == 2:
    if len(pacientes) > 0:
      cedula = None
      while True:
        try:
          cedula = int(input("Digite la cedula a buscar : "))
        except ValueError:
          print("\nSolo se recibe numeros enteros")
        else:
          break
      encontroCedula = None
      for i in range(len(pacientes)):
        if pacientes[i][0] == cedula:
          print(f"El nombre del paciente es: {pacientes[i][1]}")
          encontroCedula = 1
          break
      if encontroCedula is None:
        print("No se ha encontrado la cedula")
    else:
      print("No hay ningun paciente registrado")
  if opcion == 3:
    if len(pacientes) > 0:
      cedula = None
      while True:
        try:
          cedula = int(input("Digite la cedula a borrar : "))
        except ValueError:
          print("\nSolo se recibe numeros enteros")
        else:
          break
      encontroCedula = None
      for i in range(len(pacientes.copy())):
        if pacientes[i][0] == cedula:
          print(f"El paciente {pacientes[i][1]} con cedula {pacientes[i][0]}")
          print("Ha sido borrado con exito!")
          pacientes.pop(i)
          encontroCedula = 1
          break
      if encontroCedula is None:
        print("No se ha encontrado la cedula")
    else:
      print("No hay ningun paciente registrado")
  if opcion == 4:
    if len(pacientes) > 0:
      pacientes.sort()
      print("——— Pacientes ———\n")
      print(f"Total: {len(pacientes)}")
      for i in range(len(pacientes)):
        print(f"{i+1}. Nombre: {pacientes[i][1]} | Cedula: {pacientes[i][0]}")
        #print(f"Problemas: {pacientes[i][2]}")
      print("")
    else:
      print("No hay ningun paciente registrado")
  if opcion == 5:
    if len(pacientes) > 0:
      borrarDatos = None
      while True:
        borrarDatos = input("Estas seguro de borrar todos los datos? [ Si / No ]: ")
        if borrarDatos == "Si" or borrarDatos == "sI" or borrarDatos == "SI" or borrarDatos == "si":
          remove("pacientes")
          break
        elif borrarDatos == "No" or borrarDatos == "nO" or borrarDatos == "NO" or borrarDatos == "no":
          break
        else:
          print("Caracter invalido")
          print("Por favor digitelo nuevamente")
    else:
      print("No hay ningun dato para borrar")

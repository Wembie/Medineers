print("Hola Wembie")
import marshal
import os.path as path
from os import remove
def menu():
  print("1. Registrar paciente")
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
while opcion != 0:
  menu()
  while True:
    try:
      opcion = int(input("Digite el numero deseado [0,1,2,3,4,5]: "))
    except ValueError:
      print("Solo se recibe numeros enteros")
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
        print("Solo se recibe numeros enteros")
      else:
        for i in range(len(pacientes)):
          if pacientes[i][0] == cedula:
            print(f"La cedula {cedula} ya esta registrada")
            encontroCedula = 1
            break
        if encontroCedula is None:
          break
    print(f"El paciente {nombreCompleto}")
    print("Ha sido registrado con exito!")
    paciente.append(cedula)
    paciente.append(nombreCompleto)
    pacientes.append(paciente)
    archivo = open("pacientes","bw")
    marshal.dump(pacientes,archivo)
    archivo.close()
  if opcion == 2:
    cedula = None
    while True:
      try:
        cedula = int(input("Digite la cedula a buscar : "))
      except ValueError:
        print("Solo se recibe numeros enteros")
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
  if opcion == 3:
    cedula = None
    while True:
      try:
        cedula = int(input("Digite la cedula a borrar : "))
      except ValueError:
        print("Solo se recibe numeros enteros")
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
  if opcion == 4:
    print("——— Pacientes ———")
    for i in range(len(pacientes)):
      print(f"{i+1}. Nombre: {pacientes[i][1]} Cedula: {pacientes[i][0]}")
      #print("Problemas: {pacientes[i][2]}")
    print("")
  if opcion == 5:
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
      
      
    
    
      
    

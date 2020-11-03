#Developed by:

#Wembie.
#Juan Jose Restrepo.
#Daniela Gomez.
#Jose Miguel Lopez.


import marshal
import os
import os.path as path
from os import remove

def nuevoUsuario():
  usuario = input("Digite su usuario: ")
  password = None
  mayuscula = 0
  minuscula = 0
  numero = 0
  espacio = 0
  while True:
    password = input("Digite su contraseña: ")
    if len(password) < 8:
      print("La contraseña debe tener al menos mas de 8 caracteres")
    else:
      for contenido in password:
        if contenido.islower() == True:
          minuscula += 1
        elif contenido.isupper() == True:
          mayuscula += 1
        elif contenido.isdigit() == True:
          numero += 1
        else:
          if contenido.isspace() == True:
            espacio += 1
      if minuscula >= 1:
        if mayuscula >= 1:
          if numero >= 1:
            if espacio >= 1:
              print("La contraseña no puede tener espacios en blanco")
            else:
              break
          else:
            print("La contraseña debe tener como minimo un caracter numerico")
        else:
          print("La contraseña debe tener como minimo un caracter en mayuscula")
      else:
        print("La contraseña debe tener como minimo un caracter en minuscula")
  if path.exists("usuarios"):
    print("")
  else:
    os.mkdir("usuarios")
  archivo = open(f"usuarios/{usuario}", "w")
  archivo.write(usuario + "\n")
  archivo.write(password)
  archivo.close()  

def loguearse(usuario, password):
  listaArchivos = os.listdir("usuarios")
  if len(listaArchivos) > 0:
    if usuario in listaArchivos:
      archivo = open(f"usuarios/{usuario}", "r")
      verificacion = archivo.read().splitlines()
      if password in verificacion:
        print("\nTe has logueado con exito")
        break
      else:
        print("Contraseña incorrecta")
    else:
      print("Usuario incorrecto")
  else:
    print("No hay usuarios en la base de datos")
  
def bienvenida():
  print("—————— SOFTWARE BY MEDINEERS ——————")
  print("")
  print("——————————— Bienvenid@ ————————————")
  print("——————————————— a —————————————————")
  print("——————————— Psycho 19 —————————————")

def menuPrincipal():
  print("\n1. Iniciar sesion")
  print("2. Registrarse")
  print("0. Salir.")
  
def menu():
  print("\n1. Registrar paciente")
  print("2. Buscar paciente")
  print("3. Borrar paciente")
  print("4. Ver total pacientes")
  print("5. Borrar datos")
  print("0. Salir.")

bienvenida()
opcionPrincipal = None
while True:
  menuPrincipal()
  while True:
    try:
      opcionPrincipal = int(input("\nDigite el numero deseado [0,1,2]: "))
      print("")
    except ValueError:
      print("\nSolo se recibe numeros enteros")
    else:
      if opcionPrincipal >=0 and opcionPrincipal <= 2:
        break
      else:
        print("Numero invalido")
        print("Por favor digitelo nuevamente")
  if opcionPrincipal == 1:
    usuario = input("Digite su usuario: ")
    password = input("Digite su contraseña: ")
    loguearse(usuario, password)
  if opcionPrincipal == 2:
    nuevoUsuario()
  if opcionPrincipal == 0:
    exit()
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

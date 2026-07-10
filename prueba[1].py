alumnos = {}
asignatura={}
alumno_asignatura = {}

def mostrar_menu():
    print("MENU CALIFICACIONES")
    print("1. Agregar alumnos ")
    print("2. Agregar asignatura ")
    print("3. Agregar notas ")
    print("4. Calcular promedio ")
    print("5. Salir ")

def elegir_opcion():
    seguir = True
    while seguir:
        try:
            opcion = int(input("Ingrese Opcion "))
            seguir = False
        except:
            print("ERROR:  Opcion invalida ")
    return opcion


def validar_codigo(cod_alumno):
    try:
        cod_alumno = int(cod_alumno)
        return True
    except:
        return False
    
def agregar_alumno(alumnos):
    cod_alumno = input("Ingrese codigo alumno ")
    if validar_codigo(cod_alumno):
        cod_alumno = int(cod_alumno)
        nom_alumno = input("Ingrese nombre alumno ")
        edad_alumno = input("Ingrese edad   alumno ")
        dato_alumno = {"nombre":nom_alumno,"edad":edad_alumno}
        alumnos[cod_alumno] = dato_alumno
        return alumnos
    else:
        print("ERROR: Codigo alumno debe ser un numero entero")

    
# Programa Principal
opcion = 0
while opcion != 5:
     mostrar_menu()
     opcion = elegir_opcion()
     match opcion:
         case 1: 
            alumnos = agregar_alumno(alumnos)   
            print(alumnos)
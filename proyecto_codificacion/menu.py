from archivos import CargarDatos, GuardarResultadosEnArchivo
from codificar_decodificar import Codificar, DeCodificar

def Menu():

    lista_registros = None
    salir = False

    while not salir:

        print("============================================")
        print("                MENÚ PRINCIPAL")
        print("============================================")
        print("1. Cargar datos")
        print("2. Codificar")
        print("3. Decodificar")
        print("4. Guardar resultados en archivo")
        print("5. Salir")
        print("============================================")
        print("Seleccione una opción:")

        opcion = input().strip()

        if opcion == "1":
            lista_registros = CargarDatos()
            print("Datos cargados correctamente.")

        elif opcion == "2":
            if lista_registros is None:
                print("Debe cargar datos primero.")
            else:
                for registro in lista_registros:
                    Codificar(registro)
                print("Codificación completada.")

        elif opcion == "3":
            if lista_registros is None:
                print("Debe cargar datos primero.")
            else:
                for registro in lista_registros:
                    if registro.estado == "codificada":
                        DeCodificar(registro)
                    else:
                        print("El registro no está codificado:", registro.cadena_original)
                print("Decodificación completada.")

        elif opcion == "4":
            if lista_registros is None:
                print("No hay datos para guardar.")
            else:
                print("Ingrese ruta del archivo de salida:")
                ruta = input().strip()
                GuardarResultadosEnArchivo(ruta, lista_registros)
                print("Resultados guardados correctamente.")

        elif opcion == "5":
            salir = True

        else:
            print("Opción inválida. Intente nuevamente.")


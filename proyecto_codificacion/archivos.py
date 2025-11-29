from registro import RegistroCadena

# Leer archivo
def LeerCadenasDesdeArchivo(ruta_archivo):

    try:
        with open(ruta_archivo, "r") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        raise Exception("El archivo no existe.")

    lista = []

    for linea in lineas:
        cadena = linea.strip()
        if cadena != "":
            lista.append(cadena)

    return lista


# Guardar resultados
def GuardarResultadosEnArchivo(ruta_salida, lista_registros):

    with open(ruta_salida, "a") as f:

        for registro in lista_registros:
            f.write(f"Cadena original: {registro.cadena_original}\n")
            f.write(f"Cadena codificada: {registro.cadena_codificada}\n")
            f.write(f"Cadena decodificada: {registro.cadena_decodificada}\n")

            f.write(f"F: {registro.F}\n")
            f.write(f"MapSub: {registro.MapSub}\n")
            f.write(f"Unicos: {registro.unicos}\n")
            f.write(f"Salida paso a paso: {registro.salida}\n")

            f.write(f"Estado final: {registro.estado}\n")
            f.write("------------------------------------------\n")



# Cargar datos
def CargarDatos():

    print("¿Desea cargar desde archivo (A) o por consola (C)?")
    opcion = input().strip().upper()

    lista_cadenas = []

    if opcion == "A":
        print("Ingrese ruta del archivo:")
        ruta = input().strip()
        lista_cadenas = LeerCadenasDesdeArchivo(ruta)

    elif opcion == "C":
        print("¿Cuántas cadenas desea ingresar? (máx. 10)")
        n = int(input())

        if n > 10:
            raise Exception("Máximo 10 cadenas permitidas.")

        for _ in range(n):
            print("Ingrese cadena numérica:")
            cadena = input().strip()
            lista_cadenas.append(cadena)

    else:
        raise Exception("Opción inválida.")

    lista_registros = [RegistroCadena(cadena) for cadena in lista_cadenas]

    return lista_registros
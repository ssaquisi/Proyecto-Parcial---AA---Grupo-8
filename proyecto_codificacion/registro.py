# Estructura de datos aumentada
class RegistroCadena:
    def __init__(self, cadena):
        self.cadena_original = cadena
        self.cadena_codificada = ""
        self.cadena_decodificada = ""

        self.F = [None] * 10
        self.MapSub = [None] * 10
        self.unicos = []
        self.salida = []

        self.longitud = len(cadena)
        self.estado = "original"


# Actualizar estado
def ActualizarEstado(registro, nuevo_estado):
    registro.estado = nuevo_estado
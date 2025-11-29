from huffman import ConstruirHuffman
from registro import ActualizarEstado

# Función: primeras apariciones
def EscanearPrimerasApariciones(cadena):
    F = [None] * 10

    for pos in range(len(cadena)):
        d = int(cadena[pos])

        if F[d] is None:
            F[d] = pos

    return F


# Función: Buscar sustituto
def BuscarSustituto(d, ConjuntoOriginales, SustitutosUsados, inicio):
    s = inicio % 10

    for _ in range(10):
        if s not in ConjuntoOriginales and s not in SustitutosUsados:
            return s
        s = (s + 1) % 10

    raise Exception("No existe un sustituto disponible.")

    # Función: Codificar
def Codificar(registro):

    if registro.estado != "original":
        raise Exception("El registro no está en estado 'original'.")

    cadena = registro.cadena_original

    F = EscanearPrimerasApariciones(cadena)
    registro.F = F

    ConjuntoOriginales = {d for d in range(10) if F[d] is not None}

    unicos = sorted(ConjuntoOriginales, key=lambda d: F[d])
    registro.unicos = unicos

    HuffmanCodificar, _ = ConstruirHuffman(unicos)

    salida = []
    SustitutosUsados = set()
    MapSub = [None] * 10

    for pos in range(len(cadena)):
        d = int(cadena[pos])

        if F[d] == pos:
            codigo = HuffmanCodificar(d)
            salida.append(codigo)

        else:
            inicio = (d + 1) % 10
            s = BuscarSustituto(d, ConjuntoOriginales, SustitutosUsados, inicio)

            MapSub[s] = d
            SustitutosUsados.add(s)

            codigo = HuffmanCodificar(s)
            salida.append(codigo)

    registro.salida = salida
    registro.MapSub = MapSub

    registro.cadena_codificada = "".join(salida)
    ActualizarEstado(registro, "codificada")

    return registro


# Función: Decodificar
def DeCodificar(registro):

    if registro.estado != "codificada":
        raise Exception("El registro debe estar en estado 'codificada'.")

    salida_codificada = registro.cadena_codificada
    F = registro.F
    MapSub = registro.MapSub
    unicos = registro.unicos

    _, HuffmanDecodificar = ConstruirHuffman(unicos)

    n = len(salida_codificada)
    salida = [None] * n

    for pos in range(n):

        simbolo = HuffmanDecodificar(salida_codificada[pos])

        if F[simbolo] == pos:
            salida[pos] = str(simbolo)

        elif MapSub[simbolo] is not None:
            salida[pos] = str(MapSub[simbolo])

        else:
            raise Exception("Símbolo inválido durante la decodificación.")

    registro.cadena_decodificada = "".join(salida)
    ActualizarEstado(registro, "decodificada")

    return registro



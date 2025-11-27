
# Pseudocódigo del algoritmo Codificar - Grupo #8

FUNCIÓN Codificar(cadena):
    F = EscanearPrimerasApariciones(cadena)
    ConjuntoOriginales = { d | F[d] ? null }
    unicos = dígitos en ConjuntoOriginales ordenados según F[d]
    (HuffmanCodificar, HuffmanDecodificar) = ConstruirHuffman(unicos)
    salida = []
    SustitutosUsados = conjunto vacío
    MapSub = [null × 10]
    PARA pos DESDE 0 HASTA longitud(cadena)-1:
        d = entero(cadena[pos])
        SI F[d] == pos ENTONCES
            codigo = HuffmanCodificar(d)
            agregar codigo a salida
        SINO
            inicio = (d + 1) mod 10
            s = BuscarSustituto(d, ConjuntoOriginales, SustitutosUsados, inicio)
            MapSub[s] = d
            agregar s a SustitutosUsados
            codigo = HuffmanCodificar(s)
            agregar codigo a salida
        FIN SI
    FIN PARA
    RETORNAR (salida, F, MapSub, unicos)
FIN FUNCIÓN

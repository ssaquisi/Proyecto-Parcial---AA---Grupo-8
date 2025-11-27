
# Pseudocódigo del algoritmo Decodificar - Grupo #8

FUNCIÓN Decodificar(salida_codificada, F, MapSub, unicos):
    (HuffmanCodificar, HuffmanDecodificar) = ConstruirHuffman(unicos)
    n = longitud(salida_codificada)
    salida = arreglo de tamaño n
    PARA pos DESDE 0 HASTA n-1:
        simbolo = HuffmanDecodificar(salida_codificada[pos])
        SI F[simbolo] == pos ENTONCES
            salida[pos] = simbolo
        SINO SI MapSub[simbolo] ? null ENTONCES
            salida[pos] = MapSub[simbolo]
        SINO
            ERROR "Simbolo inválido durante la decodificación."
        FIN SI
    FIN PARA
    RETORNAR concatenar(salida)
FIN FUNCIÓN

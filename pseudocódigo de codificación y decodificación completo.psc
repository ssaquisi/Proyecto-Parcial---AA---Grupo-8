
# Pseudocódigo del programa completo - Grupo #8

FUNCIÓN EscanearPrimerasApariciones(cadena):
    
    F = arreglo de tamaño 10 inicializado en null

    PARA pos DESDE 0 HASTA longitud(cadena)-1:
        d = entero(cadena[pos])

        SI F[d] == null ENTONCES
            F[d] = pos
        FIN SI
    FIN PARA

    RETORNAR F
FIN FUNCIÓN

FUNCIÓN BuscarSustituto(d, ConjuntoOriginales, SustitutosUsados, inicio):
    
    s = inicio mod 10

    PARA i DESDE 0 HASTA 9:
        SI s NO está en ConjuntoOriginales Y
           s NO está en SustitutosUsados ENTONCES
            RETORNAR s
        FIN SI

        s = (s + 1) mod 10
    FIN PARA

    ERROR "No existe un sustituto disponible."
FIN FUNCIÓN

# Construcción del árbol de Huffman con los dígitos de 'unicos'.
# Para este pseudocódigo, se representa como dos funciones abstractas:
# HuffmanCodificar(simbolo)
# HuffmanDecodificar(codigo)

FUNCIÓN ConstruirHuffman(unicos):
    
    DEFINIR FUNCION HuffmanCodificar(simbolo):
        RETORNAR simbolo      

    DEFINIR FUNCION HuffmanDecodificar(codigo):
        RETORNAR codigo       

    RETORNAR (HuffmanCodificar, HuffmanDecodificar)
FIN FUNCIÓN

FUNCIÓN Codificar(cadena):
    
    F = EscanearPrimerasApariciones(cadena)
    
    ConjuntoOriginales = { d | F[d] != null }
    
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
    
    cadena_codificada = concatenar(salida)
    
    RETORNAR (salida, cadena_codificada, F, MapSub, unicos)
FIN FUNCIÓN

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

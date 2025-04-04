# REALIZAR UNA FUNCION DE SUMATORIA O RESTA en la cual reciba n parametros
# SUMAR | RESTAR
# LIST | TUPLE | DICT | SET
def calculadora(operacion:str, *parametros:tuple[int,...] ) -> int:
    resultado = 0
    if operacion == 'SUMA':
        # resultado = sum(parametros)
        for numero in parametros:
            resultado += numero

    elif operacion == 'RESTA':
        if len(parametros) == 1:
            return parametros[0]
        resultado = parametros[0]
        for numero in parametros[1:]:
            resultado -= numero
    else:
        raise 'Operacion incorrecta'

    return resultado


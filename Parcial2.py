# Parcial 2 - Estructura de Datos I
# Docente: Jose Javier Torres Vanstrahlen

def buscar_booleanos(pila):
    auxiliar = []
    cantidad = 0
    posicion = -1
    distancia_desde_tope = 0
    
    # Recorremos la pila usando exclusivamente operaciones de pila permitidas
    while len(pila) > 0:
        dato = pila.pop()
        auxiliar.append(dato)
        distancia_desde_tope += 1
        
        # Verificamos si el elemento es estrictamente un booleano
        if isinstance(dato, bool):
            cantidad += 1
            if posicion == -1:
                # El primer booleano extraído corresponde al tope (posición 1)
                posicion = distancia_desde_tope
                
    # Restauramos la pila original para que quede exactamente igual al inicio
    while len(auxiliar) > 0:
        pila.append(auxiliar.pop())
        
    return (cantidad, posicion)

def extraer_booleanos(pila):
    aux_enteros = []
    pila_booleanos = []
    
    # 1. Sacamos todo de la pila original separando enteros y booleanos
    while len(pila) > 0:
        dato = pila.pop()
        if isinstance(dato, bool):
            pila_booleanos.append(dato)
        else:
            aux_enteros.append(dato)
            
    # 2. Invertimos los enteros usando una pila auxiliar para que el tope (30) quede en el fondo
    aux_enteros_2 = []
    while len(aux_enteros) > 0:
        aux_enteros_2.append(aux_enteros.pop())
        
    while len(aux_enteros_2) > 0:
        pila.append(aux_enteros_2.pop())
        
    return pila_booleanos

# ==========================================
# PRUEBAS OBLIGATORIAS (NO MODIFICAR)
# ==========================================
pila1 = [7, True, 12, False, 5, True, 30]
pila2 = [4, 9, 1]
pila3 = []

print(buscar_booleanos(pila1), pila1)
print(buscar_booleanos(pila2), pila2)
print(buscar_booleanos(pila3), pila3)

resultado = extraer_booleanos(pila1)
print(pila1, resultado)
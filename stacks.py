# ENUNCIADO
# Existe una estructura de datos (PILA), que tiene N, cantidad de elementos.
# (Boolean, String, Int, Float). Realizar una limpieza de datos, solo dejar datos de tipo
# Boolean y String
# STACK = [True, False, 10, Hola Mundo, 10.0, Barranquilla, False]

#REQUISITOS

# 1. Analizar la pila 
# 2. Realizar limpieza de la pila 
# 3. Contar la cantidad de datos corruptos a limpiar 

#DEVELOPMENT
STACK = [True, False, 10, "Hola Mundo", 10.0, "Barranquilla", False] #TOPE
STACK_AUX =[]

amount = len(STACK)

print("LONGITUD", amount)

for i in range amount
   data = STACK.pop ()
   print("DATA ENCONTRADA" data)
   try:
       if data.isnumeric():
           print("ES UN NUMERO")
           STACK_AUX.append(data)
           print("SE GUARDO EN AUX")
           
   except:
       print("no es numerico")
       
print("ESTADO DE AUX", STACK_AUX)
       
       


 
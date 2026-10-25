def ejecutar_menu():
    
    pila = []
    
    while True:
        print("\n===== MENÚ DE LA PILA =====")
        print("1. Apilar un entero positivo")
        print("2. Apilar un booleano (True o False)")
        print("3. Desapilar (pop)")
        print("4. Ver el tope (peek)")
        print("5. Mostrar la pila")
        print("6. ¿Está vacía?")
        print("7. Tamaño de la pila")
        print("0. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            
            entrada = input("Ingresa un entero positivo: ").strip()
            
            if entrada.isdigit():
                numero = int(entrada)
                if numero > 0:
                    pila.append(numero)  
                    print(f"¡Éxito! Se apiló el entero positivo: {numero}")
                else:
                    print("Error: El número debe ser mayor que 0.")
            else:
                print("Error: Entrada no válida. Ingrese solo números enteros positivos (sin letras, negativos ni decimales).")
                
        elif opcion == "2":
           
            entrada = input("Ingresa un booleano (True o False): ").strip()
            if entrada == "True":
                pila.append(True)  
                print("¡Éxito! Se apiló: True")
            elif entrada == "False":
                pila.append(False) 
                print("¡Éxito! Se apiló: False")
            else:
                print("Error: Entrada no válida. Debe escribir exactamente 'True' o 'False' (respetando mayúsculas).")
                
        elif opcion == "3":
            
            if len(pila) == 0:  
                print("Aviso: La pila está vacía, no se puede desapilar.")
            else:
                elemento = pila.pop()  
                print(f"Elemento desapilado con éxito: {elemento}")
                
        elif opcion == "4":
            
            if len(pila) == 0:  
                print("Aviso: La pila está vacía, no hay elemento en el tope.")
            else:
                tope = pila[-1]  
                print(f"El tope actual de la pila es: {tope}")
                
        elif opcion == "5":
            
            if len(pila) == 0:
                print("La pila está vacía.")
            else:
                print("Contenido de la pila (del fondo al tope):", pila)
                
        elif opcion == "6":
            
            if len(pila) == 0:  
                print("Sí, la pila está vacía.")
            else:
                print("No, la pila contiene elementos.")
                
        elif opcion == "7":
            
            tamanio = len(pila)  # Comando permitido: len(lista)
            print(f"El tamaño actual de la pila es: {tamanio}")
            
        elif opcion == "0":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Error: Opción de menú no válida. Por favor, elige una opción del 0 al 7.")

if __name__ == "__main__":
    ejecutar_menu()
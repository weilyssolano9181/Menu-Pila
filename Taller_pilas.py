
pila = [4, 8, 15]
pila.append(16)

pila.append(23)
pila.append(42)

pila.pop()
pila.pop()

print("El tope de la pila es:", pila[-1])
pila.append(5)

print("¿La pila está vacía?:", len(pila) == 0)

print("Pila final:", pila)
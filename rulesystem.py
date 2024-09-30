class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = {}  # Diccionario de conexiones: {nodo: distancia}

    def agregar_conexion(self, nodo, distancia):
        self.conexiones[nodo] = distancia

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        self.nodos[nombre] = Nodo(nombre)

    def agregar_conexion(self, origen, destino, distancia):
        if origen not in self.nodos:
            self.agregar_nodo(origen)
        if destino not in self.nodos:
            self.agregar_nodo(destino)
        self.nodos[origen].agregar_conexion(self.nodos[destino], distancia)
        self.nodos[destino].agregar_conexion(self.nodos[origen], distancia)  # Camino bidireccional

def mejor_ruta(grafo, inicio, fin):
    visitados = set()  # Conjunto para nodos visitados
    rutas = {inicio: (None, 0)}  # Nodo: (nodo anterior, distancia)

    while rutas:
        # Selecciona el nodo con la distancia más corta
        nodo_actual = min(rutas, key=lambda x: rutas[x][1])
        distancia_actual = rutas[nodo_actual][1]

        # Si hemos llegado al nodo final, construimos la ruta
        if nodo_actual == fin:
            ruta = []
            ruta.append(nodo_actual)
            nodo_actual = rutas[nodo_actual][0]
            return ruta[::-1], distancia_actual  # Retorna la ruta y la distancia

        # Marcamos el nodo actual como visitado
        visitados.add(nodo_actual)
        print(f"Nodo actual: {nodo_actual}, Rutas: {rutas}, Visitados: {visitados}")

        # Procesar las conexiones del nodo actual
        for vecino, distancia in grafo.nodos[nodo_actual].conexiones.items():
            if vecino.nombre not in visitados:
                nueva_distancia = distancia_actual + distancia
                # Si la nueva distancia es menor, actualizamos la ruta
                if vecino.nombre not in rutas or nueva_distancia < rutas[vecino.nombre][1]:
                    rutas[vecino.nombre] = (nodo_actual, nueva_distancia)

        # Ya no necesitamos el nodo actual para la siguiente iteración
        del rutas[nodo_actual]

    return None, float('inf')  # No hay ruta encontrada

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_conexion('A', 'B', 1)
grafo.agregar_conexion('A', 'C', 4)
grafo.agregar_conexion('B', 'C', 2)
grafo.agregar_conexion('B', 'D', 5)
grafo.agregar_conexion('C', 'D', 1)

ruta, distancia = mejor_ruta(grafo, 'A', 'C')
if ruta:
    print(f"La mejor ruta de A a D es: {ruta} con una distancia de {distancia}.")
else:
    print("No se encontró una ruta.")

import time
from collections import deque

class Proceso:

    def __init__(self,nombre,tiempo,prioridad,datos):
        self.nombre = nombre
        self.tiempo = tiempo
        self.prioridad = prioridad
        self.datos = datos
        self.estado = "Nuevo"

    def mostrar(self):

        print(f"{self.nombre} | Estado: {self.estado} | Tiempo restante: {self.tiempo}")

# procesos del SIGET
p1 = Proceso("AlertaSemaforo",4,"Alta",200)
p2 = Proceso("TraficoCentro",6,"Media",500)
p3 = Proceso("CamaraAccidente",3,"Alta",150)

procesos=[p1,p2,p3]

# -----------------------
# FIFO
# -----------------------

def fifo(lista):

    print("\n--- ALGORITMO FIFO ---\n")

    for p in lista:

        p.estado="Listo"
        p.mostrar()

    for p in lista:

        p.estado="En ejecución"

        while p.tiempo>0:

            p.mostrar()
            time.sleep(1)

            p.tiempo-=1

        p.estado="Terminado"
        p.mostrar()

# -----------------------
# ROUND ROBIN
# -----------------------

def round_robin(lista,quantum):

    print("\n--- ALGORITMO ROUND ROBIN ---\n")

    cola=deque(lista)

    while cola:

        p=cola.popleft()

        if p.tiempo>0:

            p.estado="En ejecución"

            for i in range(quantum):

                if p.tiempo>0:

                    p.mostrar()
                    time.sleep(1)

                    p.tiempo-=1

            if p.tiempo>0:

                p.estado="Listo"
                cola.append(p)

            else:

                p.estado="Terminado"
                p.mostrar()

# ejecutar simulacion

fifo(procesos)

# reiniciar tiempos
p1.tiempo=4
p2.tiempo=6
p3.tiempo=3

round_robin(procesos,2)
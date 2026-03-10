import threading
import time
import random
from queue import Queue

# buffer compartido
buffer = Queue(maxsize=5)

def productor(nombre):

    while True:

        dato = random.randint(1,100)

        buffer.put(dato)

        print(f"{nombre} envio dato de trafico: {dato}")

        time.sleep(random.uniform(0.5,2))

def consumidor():

    while True:

        dato = buffer.get()

        print(f" Analizador SIGET procesando dato: {dato} ")

        time.sleep(1.5)

# hilos productores
p1 = threading.Thread(target=productor,args=("Sensor Norte",))
p2 = threading.Thread(target=productor,args=("Sensor Centro",))

# hilo consumidor
c1 = threading.Thread(target=consumidor)

p1.start()
p2.start()
c1.start()
"""
    Solución: cambiar de primitiva de concurrencia (lock -> semáforo)
"""

# Librerías
from time import sleep
from threading import Thread
from threading import Lock
from threading import Semaphore
import threading
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-1s (%(threadName)s) %(message)s',
)

# uso
logging.debug('Starting program')


def tarea(sem):
    sleep(0.01)  # tareas tardadas
    for i in range(ITERATIONS):  # trabajo
        sleep(0.01)  # más tareas tardadas
        with sem:  # primitiva de concurrencia
            logging.debug(f'Working {i}')  # acción crítica
        sleep(0.01)  # más tareas tardadas


ITERATIONS = 5
HILOS = 3

logging.debug('Ejemplo de Starvation')

# Crear un semáforo (primitiva de concurrencia)
sem = Semaphore(HILOS)

# Crear hilos
for i in range(HILOS):
    thread = Thread(name=f"hilo-{i}", target=tarea, args=(sem,))
    thread.start()

# Esperar a que terminen los hilos
for thread in threading.enumerate():
    # if thread name starts with 'Thread' join it
    if thread.name.startswith('hilo'):
        #logging.debug(f'Esperando a que termine {thread.name}')
        thread.join()

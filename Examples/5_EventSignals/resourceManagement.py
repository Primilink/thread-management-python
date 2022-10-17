import threading
import time
import logging
import random


def consumidor(cond):
    """espera por la condición y utilizar el recurso"""
    logging.debug('Iniciando hilo consumidor')
    with cond:
        cond.wait()
        logging.debug('Recurso disponible para el consumidor')


def productor(cond):
    """coloca el recurso a ser utilizado por el consumidor"""
    logging.debug('Iniciando hilo productor')
    with cond:
        logging.debug('Haciendo el recurso disponible')
        cond.notify_all()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condicion = threading.Condition()
c1 = threading.Thread(name='c1', target=consumidor, args=(condicion,))
c2 = threading.Thread(name='c2', target=consumidor, args=(condicion,))
p = threading.Thread(name='p', target=productor, args=(condicion,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()

"""
Output:

2022-10-17 15:27:06,174 (c1) Iniciando hilo consumidor
2022-10-17 15:27:06,378 (c2) Iniciando hilo consumidor
2022-10-17 15:27:06,580 (p ) Iniciando hilo productor
2022-10-17 15:27:06,580 (p ) Haciendo el recurso disponible
2022-10-17 15:27:06,580 (c2) Recurso disponible para el consumidor
2022-10-17 15:27:06,580 (c1) Recurso disponible para el consumidor

"""

import threading
import time
import logging


def trabajador():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")


def mi_servicio():
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug("Exiting")


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',
)

s = threading.Thread(name='mi_servicio__str__', target=mi_servicio)
h = threading.Thread(name='trabajador__str__', target=trabajador)
h2 = threading.Thread(target=trabajador)

h.start()
h2.start()
s.start()

"""
Output:

2022-10-17 11:37:53,291 [DEBUG] (trabajador__str__) Starting
2022-10-17 11:37:53,291 [DEBUG] (Thread-1 (trabajador)) Starting
2022-10-17 11:37:53,292 [DEBUG] (mi_servicio__str__) Starting
2022-10-17 11:37:53,495 [DEBUG] (Thread-1 (trabajador)) Exiting
2022-10-17 11:37:53,495 [DEBUG] (trabajador__str__) Exiting
2022-10-17 11:37:53,607 [DEBUG] (mi_servicio__str__) Exiting
"""

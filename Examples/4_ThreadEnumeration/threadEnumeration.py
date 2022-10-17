import threading
import time
import logging
import random


def trabajador():
    """funcion del trabajador"""
    pausa = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pausa)
    time.sleep(pausa)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    h = threading.Thread(target=trabajador, daemon=True)
    h.start()

hilo_principal = threading.main_thread()
for h in threading.enumerate():
    if h is hilo_principal:
        continue
    logging.debug('joining %s', h.name)
    h.join()

"""
Output:

Thread-1 (trabajador)) sleeping 0.50
(Thread-2 (trabajador)) sleeping 0.30
(Thread-3 (trabajador)) sleeping 0.10
(MainThread) joining Thread-1 (trabajador)
(Thread-3 (trabajador)) ending
(Thread-2 (trabajador)) ending
(Thread-1 (trabajador)) ending
(MainThread) joining Thread-2 (trabajador)
(MainThread) joining Thread-3 (trabajador)
"""

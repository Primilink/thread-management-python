import threading
import time


def trabajador():
    print(threading.current_thread().name + 'Starting w.')
    time.sleep(0.2)
    print(threading.current_thread().name + 'Exiting w.')


def mi_servicio():
    print(threading.current_thread().name + 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().name + 'Exiting')


s = threading.Thread(name='1 mi_servicio--str--', target=mi_servicio)
h = threading.Thread(name='2 trabajador--str--', target=trabajador)
h2 = threading.Thread(target=trabajador)

h.start()
h2.start()
s.start()

"""
Output:

2 trabajador--str--Starting w.
Thread-1 (trabajador)Starting w.
1 mi_servicio--str--Starting
Thread-1 (trabajador)Exiting w.
2 trabajador--str--Exiting w.
1 mi_servicio--str--Exiting
"""

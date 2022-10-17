import threading


def trabajador(num):
    """funcion del hilo"""
    print("Trabajador: %s" % num)


hilos = []
for i in range(5):
    # when using args, you need to use an iterable object (list, tuple, etc.)
    h = threading.Thread(target=trabajador, args=(i,))
    # h = threading.Thread(target=trabajador, args=([i])) # this works too
    hilos.append(h)
    h.start()

"""
Output:

    Trabajador: 0
    Trabajador: 1
    Trabajador: 2
    Trabajador: 3
    Trabajador: 4
"""

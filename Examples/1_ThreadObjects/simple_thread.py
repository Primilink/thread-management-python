import threading


def trabajador():
    """funcion del hilo"""
    print("Trabajador")


hilos = []
for i in range(5):
    h = threading.Thread(target=trabajador)
    hilos.append(h)
    h.start()


"""
Output:

    Trabajador
    Trabajador
    Trabajador
    Trabajador
    Trabajador
"""

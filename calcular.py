import math
# solo que hay que usar variables globales creo para tkinter
h = 1
def cita3(o2p,o4p,cita2):
    return math.sin((o2p*math.sin(cita2)-h)/(o4p))**-1

# Velocidad angular 3
def w3(w2,o2p,o4p,cita2,cita3):
    return ((-w2*o2p*math.cos(cita2))/(o4p*math.cos(cita3)))

def velocidadA(w2,o2p):
    return w2*o2p

def velocidadB(w2,o2p,w3,o4p,cita2,cita3):
    return (-w2*o2p*math.sin(cita2) - w3*o4p*math.sin(cita3))

def alfa3(w2, o2p, w3, o4p, cita2, cita3):
    return ( (w2**2*o2p*math.sin(cita2) - w3**2*o4p*math.sin(cita3) / (o4p*math.cos(cita3) )))

def aceleracionP(w2,o2p,cita2):
    return ( math.sqrt( (-w2**2*o2p*math.cos(cita2))**2 + (-w2**2*o2p*math.sin(cita2))**2 ) )

def aceleracionO4(w2, o2p, cita2, alfa3, o4p, cita3, w3):
    return -w2**2*o2p*math.cos(cita2) - alfa3*o4p*math.sin(cita3) - w3**2*o4p*math.cos(cita3)



# # Da la persona
# distanciaO2P = 0
# distanciaO4P = 0
# # Constante
# hConstante = 1

# # Da el usuario
# zeta2 = input()
# # Calcular
# zeta3 = 0

# # Da el usuario
# velocidadAngular2 = input()
# # Calcular
# velocidadAngular3 = 0

# velocidadA = velocidadAngular2 * distanciaO2P
# # Cal
# velocidadB = 0

# # Constante
# alfa2 = 0
# # Calcular
# alfa3 = 0

# # Calcular
# aceleracionP = 0
# aceleracionO4 = 0
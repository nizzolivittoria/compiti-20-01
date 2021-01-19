import math

def calcolo_delta(a, b, c):
    der = math.pow(b, 2) - 4 * a * c
    return der

def calcolo_vertice(a, b, c):
    delta = calcolo_delta(a, b, c)
    Xv = -(b/(2*a))
    Yv = -(delta/(4*a))
    return Xv, Yv

def calcolo_fuoco(a, b, c):
    delta = calcolo_delta(a, b, c)
    Xf = -(b/(2*a))
    Yf = (1 - delta)/(4*a)
    return Xf, Yf

def main():
    a = int(input("inserisci a"))
    b = int(input("inserisci b"))
    c = int(input("inserisci c"))

    scelta = int(input("cosa vuoi calcolare? premi 1 per sapere il vertice, 2 per il fuoco, per abbandonare premi 0 e premi 3 per conoscere vertice e fuoco"))
    if scelta == 1:
        print(calcolo_vertice(a, b, c))
    elif scelta == 2:
        print(calcolo_fuoco(a, b, c))
    elif scelta == 0:
        print("addio")
    elif scelta == 3:
        print(calcolo_vertice(a, b, c))
        print(calcolo_fuoco(a, b, c))
    else:
        print("hai sbagliato scusa")   

main()

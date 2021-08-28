import numpy as np

def leEntrada():
    num_elementos, num_conjuntos = input().split()

    num_elementos = int(num_elementos)
    num_conjuntos = int(num_conjuntos)
    capacidades = input().split()
    capacidades = np.array([int(x) for x in capacidades])
    matriz_incidencia = np.zeros((num_elementos,num_conjuntos), dtype=np.int8)

    for i in range(num_elementos):
        matriz_incidencia[i] = np.array(list(input().split()))

    return capacidades,matriz_incidencia

def main():
    capacidades,matriz_incidencia=leEntrada()
    print("Capacidades: \n{}".format(capacidades))
    print("Matriz Incidencia: \n{}".format(matriz_incidencia))
    
if __name__ == '__main__':
    main()
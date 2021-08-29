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

def get_not_covered_element_index(elements_weight):
    for i in range(elements_weight.shape[0]):
        if elements_weight[i] == 0:
            return i
    return -1

def element_is_not_covered(element_index):
    return element_index != -1

def get_max_weight_possible_of(index_elem, elements_weight, A_T, capacidades):
    sets_elements_can_be = A_T[:,index_elem]
    lines_of_sets_element_can_be = np.array([A_T[i] for i in range(A_T.shape[0]) if sets_elements_can_be[i] == 1])
    #print("sets_elements_can_be: {}".format(sets_elements_can_be))
    #print("Linhas Conjuntos que o elemento esta presente\n {}".format(lines_of_sets_element_can_be))

    max_weights = []
    #print("Pesos atuais: {}".format(elements_weight))
    for i in range(sets_elements_can_be.shape[0]):
        if sets_elements_can_be[i] == 1:
            #print("Linha vista atual: {}".format(A_T[i]))
            #print("Capacidade total: {}".format(capacidades[i]))
            max_weight_in_line = int(capacidades[i] - (elements_weight.T @ A_T[i]))
            max_weights.append(max_weight_in_line)
    max_weight = min(max_weights)
    print("Max weight: {}".format(max_weight))

    return max_weight


def main():
    capacidades,matriz_incidencia=leEntrada()
    #print("Capacidades: \n{}".format(capacidades))
    #print("Matriz Incidencia: \n{}".format(matriz_incidencia))
    #print("A_T:\n{}".format)

    A_T = matriz_incidencia.T
    #print("A_T:\n{}".format(A_T))
    elements_weight = np.zeros(matriz_incidencia.shape[0])  
    selected_sets = np.zeros(matriz_incidencia.shape[1])
    already_covered_elements = np.zeros(matriz_incidencia.shape[0])

    while True:
        index_elem_not_covered = get_not_covered_element_index(already_covered_elements)
        if element_is_not_covered(index_elem_not_covered):
            print("Elemento fora de qualquer conjunto: {}".format(index_elem_not_covered))
            element_max_weight = get_max_weight_possible_of(index_elem_not_covered, elements_weight, A_T, capacidades)
            elements_weight[index_elem_not_covered] = element_max_weight
            print("Pesos atuais: {}".format(elements_weight))
            break
        else:
            break
    
if __name__ == '__main__':
    main()
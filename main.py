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

def get_max_weight_possible_of(sets_elements_can_be, elements_weight, A_T, capacidades):
    max_weights = []
    for i in range(sets_elements_can_be.shape[0]):
        if sets_elements_can_be[i] == 1:
            max_weight_in_line = int(capacidades[i] - (elements_weight.T @ A_T[i]))
            max_weights.append(max_weight_in_line)
    max_weight = min(max_weights)
    return max_weight


def find_new_set(sets_elements_can_be, A_T, elements_weight, capacidades, selected_sets):
    for i in range(sets_elements_can_be.shape[0]):
        if sets_elements_can_be[i] == 1:
            line = A_T[i]
            sum = line @ elements_weight
            if sum == capacidades[i] and selected_sets[i] == 0:
                return i
    return -1

def define_new_elements_covered_by_set(set_elements, already_covered_elements):
    return np.array([1 if set_elements[i] == 1 or already_covered_elements[i] == 1 else 0 for i in range(set_elements.shape[0])])

def stringVetor(vetor):
        saida = ""
        saida +="{}".format(vetor[0])
        for i in range(1,vetor.shape[0]):
            saida +=" {}".format(vetor[i])
        return saida

def main():
    capacidades,matriz_incidencia=leEntrada()

    A_T = matriz_incidencia.T
    elements_weight = np.zeros(matriz_incidencia.shape[0], dtype = np.int32)  
    selected_sets = np.zeros(matriz_incidencia.shape[1], dtype = np.int8)
    already_covered_elements = np.zeros(matriz_incidencia.shape[0])

    while True:
        index_elem_not_covered = get_not_covered_element_index(already_covered_elements)
        if element_is_not_covered(index_elem_not_covered):
            sets_elements_can_be = A_T[:,index_elem_not_covered]
            lines_of_sets_element_can_be = np.array([A_T[i] for i in range(A_T.shape[0]) if sets_elements_can_be[i] == 1])
            element_max_weight = get_max_weight_possible_of(sets_elements_can_be, elements_weight, A_T, capacidades)
            elements_weight[index_elem_not_covered] = element_max_weight
            new_set_found_index = find_new_set(sets_elements_can_be, A_T, elements_weight, capacidades, selected_sets)
            if new_set_found_index != -1:
                selected_sets[new_set_found_index] = 1
                set_elements = A_T[new_set_found_index]
                already_covered_elements = define_new_elements_covered_by_set(set_elements, already_covered_elements)
        else:
            break
    print(stringVetor(selected_sets))
    print(stringVetor(elements_weight))
    
if __name__ == '__main__':
    main()
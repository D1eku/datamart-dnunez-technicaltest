
"""
INDICACIONES:
1. Implemente su solución para los problemas 1, 2, 3, 7 y 8 en Python3.
3. Analice la complejidad computacional de cada operación implementada en su solución al problema 3.
4. Implemente un algoritmo que reciba en la entrada dos listas de números enteros y haga un map de cada elemento de
la segunda lista con la función del problema 8 utilizando la primera lista como dominio de la búsqueda.
Teniendo en cuenta que el tamaño de la primera lista podría ser muy grande explique qué beneficios tiene
utilizar una búsqueda binaria en lugar de utilizar una búsqueda secuencial y cómo impacta la complejidad
computacional de la solución. En circunstancias donde el segundo listado sea también
grande es conveniente procesar las peticiones en paralelo; en este escenario sería conveniente poder 
configurar una máxima cantidad de workers para que procesen de forma paralela el segundo arreglo. 
Proponga una solución general a este problema utilizando Python3

"""

# 1. Escribe una función llamada merge_arrays que acepte dos arrays ordenados de enteros como parámetros y devuelva un solo array ordenado que contenga todos los elementos de ambos.
def merge(arrayA, arrayB):
    output = []
    
    indexA = 0
    indexB = 0
    while(indexA < len(arrayA) and indexB < len(arrayB)):
        if(arrayA[indexA] < arrayB[indexB]):
            output.append(arrayA[indexA])
            indexA +=1
        else:
            output.append(arrayB[indexB])
            indexB +=1
    
    while(indexA < len(arrayA)):
        output.append(arrayA[indexA])
        indexA +=1

    while(indexB < len(arrayB)):
        output.append(arrayB[indexB])
        indexB +=1
        
    return output
    
print("\n\n Problem 1: Merge")
print("respuesta: ",merge([3, 4, 5], [1,8,9]))


# 2. Escribe una función llamada find_median que acepte un array de enteros como parámetro y devuelva la mediana del conjunto.
def find_median(array):
    array.sort()
    if(len(array) % 2 != 0):
        return array[int((len(array)+ 1)/2)]
    else:
        return (array[int(len(array)/2) - 1] + array[int(len(array)/2)])/2
print("\n\n Problem 2: find median")
print("Mediana Impar: ", find_median([1 ,2 ,3 ,4 ,4, 4, 5, 6, 7, 8, 8]))
print("Mediana par: ", find_median([2, 2, 4, 4, 6, 7, 8, 9, 11, 13]))


#3. Escribe una clase llamada BinaryTree que implemente un árbol binario de búsqueda.
# La clase debe tener métodos para 
    # insertar, buscar, debe ser capaz de imprimir el árbol en orden ascendente.
class BinaryTree:

    def __init__(self):
        self.root = None
    
    def print_ascend(self):
        target = self.root
        if(target == None):
            print("[]")
        else:
            self.__print_ascend( target)

    def __print_ascend(self, target):
            if(target != None):
                self.__print_ascend(target.left)
                print(target.value)
                self.__print_ascend(target.right)


    def find(self, value):
        if(self.root == None):
            return False
        else:
            target = self.root
            while(target != None):
                if(target.value == value):
                    return True
                else:
                    if(value < target.value):
                        target = target.left
                    else:
                        target = target.right
        return False

    def insert(self, value):
        if(self.root == None):
            self.root = Node(value)
        else:#Hay mas de 1 elemento
            self.__insert(self.root, value)

    def __insert(self, target, value):
        if(value < target.value):
            if(target.left == None):
                target.left = Node(value)
            else:
                self.__insert(target.left, value)
        else:
            if(target.right == None):
                target.right = Node(value)
            else:
                self.__insert(target.right, value)
                
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

print("\n\nProblem 3: BinaryTree Implementation. ")
arrayTest1 = [1, 2, 3, 9, 5, 8]
print("Printing BTree Ascending For Following Array: ", arrayTest1)
btree = BinaryTree()
for x in arrayTest1:
    btree.insert(x)
btree.print_ascend()

arrayTest1 = [1, 2, 3, 9, 5, 8]
print("Printing BTree Ascending For Following Array: ", arrayTest1)
btree = BinaryTree()
for x in arrayTest1:
    btree.insert(x)
btree.print_ascend()

justification_complexity = """

Sobre la complejidad temporal, y dependiendo de si el arbol esta balanceado, 
y que tan profundo se deba recorrer para el arbol para insertar/buscar un dato, entonces podemos
 considerar que su complejidad a desde Log N hasta N. 

"""
print("Justificacion de complejidad algoritmica del BinaryTree: ")
print(justification_complexity)



# 7. Escribe una función llamada remove_duplicates que acepte una lista como parámetro y devuelva una nueva lista sin elementos duplicados.
def remove_duplicates(array):
    output = []
    for x in array:
        if(not x in output):
            output.append(x)

    return output

print("\n\nProblem 7: Remove Duplicates")
remove_duplicates_test1 = [1, 1, 1, 2, 2, 3, 3, 3 ,3 ,3 ,4 ,5 ,6, 1, 123, 3,2 , 5, 7,9]
print("Removing Duplicates for: ", remove_duplicates_test1)
print("Unique Elements for Array: ", remove_duplicates(remove_duplicates_test1))


# 8. Dada una lista de números en orden ascendente y un número objetivo, escribe una función recursiva que encuentre si el número objetivo está en la lista utilizando una búsqueda binaria.
def binary_search(list, element):
    if(len(list) == 0):
        return False
    else:
        mid_index = int(len(list)/2)
        mid_value = list[mid_index]
        if(element == mid_value):
            return True
        else:
            if(element < mid_value):
                return binary_search(list[0: mid_index], element)
            else:
                return binary_search(list[mid_index+1: len(list)], element)

print("\n\nProblem 8: ")
binary_array_test1 = [1,2,6,8,11,14,15,17, 23 ,27,39,41,44,47,89,99,1001]
print("Starting Evaluation for the following array with binary search: ",binary_array_test1)
test_elements_to_search = [8, 27, 39, 1001, 99999, -2332, 1002, 8]
for e in test_elements_to_search:
    print("The", e , "exists on array ? ", binary_search(binary_array_test1, e))



"""
4. Implemente un algoritmo que reciba en la entrada dos listas de números enteros y haga un map de cada elemento de
la segunda lista con la función del problema 8 utilizando la primera lista como dominio de la búsqueda.
Teniendo en cuenta que el tamaño de la primera lista podría ser muy grande explique qué beneficios tiene
utilizar una búsqueda binaria en lugar de utilizar una búsqueda secuencial y cómo impacta la complejidad
computacional de la solución. En circunstancias donde el segundo listado sea también
grande es conveniente procesar las peticiones en paralelo; en este escenario sería conveniente poder 
configurar una máxima cantidad de workers para que procesen de forma paralela el segundo arreglo. 
Proponga una solución general a este problema utilizando Python3
"""

print("\n\nExtra Problem with Paralelism: ")
"""
Nota: Como el enunciado no lo deja en claro, asumire que la primera lista puede tener eleentos repetidos.
por lo que solo retornare una lista paralela en tamaño al primer arreglo, que tendra los true/false sies que existe cada elemento.
en el segundo array.

Ademas, considerare que el segundo arreglo debe ser un arreglo ordenado, ya que por regla para utilizar busqueda binaria
el arreglo debe estar ordenado. Si no, este se podria haber ordenado, pero asumiremos que esta ordenado y luego ejecutaremos la busqueda.

Sobre la justificacion de porque la busqueda binaria es mejor que la secuencial, pues basicamente
reduce el tiempo de busqueda a la mitad respecto a la secuencial, ya que evita la mitad de valores que sean mayor
al que se esta buscando.
"""
import concurrent.futures

def paralelism_with_arrays(a, b, workers=1):
    output = [None] * len(a)
    with concurrent.futures.ThreadPoolExecutor(workers) as executor:
        for i in range(len(a)):
            t = executor.submit(binary_search, b, a[i])
            output[i] = t.result()
    return output

print("Starting paralelism funtion...")
print("First Array: ",test_elements_to_search)
print("Second Array: ", binary_array_test1)
print("Result: ")
print(paralelism_with_arrays(test_elements_to_search, binary_array_test1, 4))
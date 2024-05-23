
"""



INDICACIONES:
1. Implemente su solución para los problemas 1, 2, 3, 7 y 8 en Python3.
2. Implemente su solución para los problemas 4, 5, 6 en Javascript o TypeScript.
3. Analice la complejidad computacional de cada operación implementada en su solución al problema 3.
4. Implemente un algoritmo que reciba en la entrada dos listas de números enteros y haga un map de cada elemento de la segunda lista con la función del problema 8 utilizando la primera lista como dominio de la búsqueda. Teniendo en cuenta que el tamaño de la
primera lista podría ser muy grande explique qué beneficios tiene utilizar una búsqueda binaria en lugar de utilizar una búsqueda secuencial y cómo impacta la complejidad computacional de la solución. En circunstancias donde el segundo listado sea también
grande es conveniente procesar las peticiones en paralelo; en este escenario sería conveniente poder configurar una máxima cantidad de workers para que procesen de forma paralela el segundo arreglo. Proponga una solución general a este problema utilizando Python3


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
    

print("respuesta: ",merge([3, 4, 5], [1,8,9]))


# 2. Escribe una función llamada find_median que acepte un array de enteros como parámetro y devuelva la mediana del conjunto.
def find_median(array):
    array.sort()
    if(len(array) % 2 != 0):
        return array[int((len(array)+ 1)/2)]
    else:
        return (array[int(len(array)/2) - 1] + array[int(len(array)/2)])/2

print("Mediana Impar: ", find_median([1 ,2 ,3 ,4 ,4, 4, 5, 6, 7, 8, 8]))
print("Mediana par: ", find_median([2, 2, 4, 4, 6, 7, 8, 9, 11, 13]))


#3. Escribe una clase llamada BinaryTree que implemente un árbol binario de búsqueda.
# La clase debe tener métodos para insertar, buscar, debe ser capaz de imprimir el árbol en orden ascendente.
class BinaryTree:

    def __init__(self):
        self.root = None
    
    def print_ascend(self):
        target = self.root
        while(target != None):
            self.__print_ascend( target, None)

    def __print_ascend(self, target, father):
        if(target.left == None and target.right == None):
            print(target.value)
        else:
            if(target.left != None):
                self.__print_ascend(target.left, target)
            else:
                print(father.value)
                self.__print_ascend(target.right, target)


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
        print("Target.value == ", target.value)
        print("Value: ", value)
        if(target == None):
            target = Node(value)
        else:
            if(target.value < value): #Revisar izquierda
                self.__insert(target.left, value)
            else: #Revisar derecha.
                self.insert(target.right, value)
                
class Node:
    value = None
    left = None
    right = None
    def __init__(self, value):
        value = value

btree = BinaryTree()
btree.insert(1)
btree.insert(2)
btree.insert(3)
btree.insert(9)
btree.insert(5)
btree.insert(8)
btree.print_ascend()

"""
# 7. Escribe una función llamada remove_duplicates que acepte una lista como parámetro y devuelva una nueva lista sin elementos duplicados.
def remove_duplicates(array):
    output = []
    for x in array:
        if(not x in output):
            output.append(x)

    return output

remove_duplicates([1, 1, 1, 2, 2, 3, 3, 3 ,3 ,3 ,4 ,5 ,6, 1, 123, 3,2 , 5, 7,9])


# 8. Dada una lista de números en orden ascendente y un número objetivo, escribe una función recursiva que encuentre si el número objetivo está en la lista utilizando una búsqueda binaria.
def binary_find(list, element):
"""
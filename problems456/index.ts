/**
 * Solucion a los problemas 4, 5 y 6 de la prueba de datamart para backend engineer.
 *
 * Problemas
 * -----------------------
 * 4.- Escribe una función llamada isAnagram que acepte dos cadenas de texto como
 * parámetros y determine si son anagramas (es decir, si tienen exactamente las
 * mismas letras, pero en diferente orden).
 *
 * 5.- Escribe una función llamada findCommonElements que acepte una lista de listas como parámetro
 * y devuelva una lista con los elementos comunes a todas las sub-listas.
 *
 * 6.- Escribe una implementación para el algoritmo de ordenamiento mergesort.
 */

/**
 * Escribe una función llamada isAnagram que acepte dos cadenas de texto como
 * parámetros y determine si son anagramas (es decir, si tienen exactamente las
 * mismas letras, pero en diferente orden).
 */
const isAnagram = (first_string: string, second_string: string) : boolean => {

  if(first_string.length != second_string.length){
    return false;
  }

  for(const character of first_string.split("")){
    if(!second_string.includes(character)){
      return false;
    }
  }

  return true;
}

/**
 * Escribe una función llamada findCommonElements que acepte una lista de listas como parámetro
 * y devuelva una lista con los elementos comunes a todas las sub-listas.
 */
const findCommonElements = (lists: any[][]) => {
  const output = [];
  const sortedList = lists.sort((a,b) => a.length - b.length)
  const sortedListLessFirst = sortedList.slice(1, sortedList.length)
  const lessItemsLit = sortedList[0];

  for(const element of lessItemsLit) {
    if(sortedListLessFirst.every((list) => list.includes(element))){ //If element exists on each list
      output.push(element)
    }
  }

  return output;
}

/**
 * Escribe una implementación para el algoritmo de ordenamiento mergesort.
 */
const mergeSort = (array: number[]) => {
  /*
  Merge sort no recursivo
   */
  const merge = (a :number[], b: number[]): number[] => {
    const output : number[] = []

    let indexA = 0;
    let indexB = 0;

    while(indexA < a.length && indexB < b.length) {
      if(a[indexA] < b[indexB]) {
        output.push(a[indexA]);
        indexA++;
      } else {
        output.push(b[indexB])
        indexB++;
      }
    }

    while (indexA < a.length  ) {
      output.push(a[indexA])
      indexA++;
    }

    while (indexB < b.length  ) {
      output.push(b[indexB])
      indexB++;
    }

    return output;
  }

  const mergeRec = (array: number[]): number[] => {
    
    if(array.length>1){
      const midIndex = Math.trunc(array.length/2)

      const p1 = mergeRec(array.slice(0, midIndex))
      const p2 = mergeRec(array.slice(midIndex, array.length))

      return merge(p1, p2)
    } else {
      return  array
    }
  }


  return mergeRec(array);
}


//Problema 4
console.log("Problem 4: is anagram")
console.log("(GATO", "TOGA)","These words are anagrams ? :-", isAnagram("GATO", "TOGA"))
console.log("(CALOR", "AMOR)","These words are anagrams ? :-", isAnagram("CALOR", "AMOR"))

//Problema 5
console.log("Problem 5: common elements")
const commonTest1 = [
  [1, 2, 3],
  ['1', 3, 'z', 3],
  [{caseName: 'word'},3]
]
console.log("Finding common elements on this array of arrays: ", commonTest1)
console.log("Commons: ", findCommonElements(commonTest1));
const commonTest2 = [
  [1, 2, 3, [], 'z'],
  ['1', 3, 'z', 3, []],
  [{caseName: 'word'}, '1', 3, 'z', 3],
  [1, [], 'z', 3]
]
console.log("Finding common elements on this array of arrays: ", commonTest2)
console.log("Commons: ", findCommonElements(commonTest2));

// Problema 6
console.log("Problem 6: merge sort")
const mergeTest1 = [12, 11,13, 5, 6 ,7]
console.log("Disordered Array1: ", mergeTest1)
console.log(mergeSort(mergeTest1))
const mergeTest2 = [1,33,25,22,88,11,665,44,227,88,6321,31,1,32,3,52,1235,1,1,312,3423]
console.log("Disordered Array2: ", mergeTest2)
console.log(mergeSort(mergeTest2))
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
export const isAnagram = (first_string: string, second_string: string) : boolean => {

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

  //Todo: improve the type because must not to be necessary the accessing to the index in twice-.
  for(const element of lessItemsLit[0]) {
    if(sortedListLessFirst.every((list) => list.includes(element)) ){
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
    while(indexA != a.length && indexB != a.length) {
      if(a[indexA] > b[indexB]) {
        output.push(a[indexA]);
        indexA++;
      }else {
        output.push(a[indexB])
        indexB++;
      }
    }

    while (indexA != a.length  ) {
      output.push(a[indexA])
      indexA++;
    }

    while (indexB != b.length  ) {
      output.push(b[indexB])
      indexB++;
    }

    return output;
  }
  const mergeRec = (array: number[]): number[] => {
    console.log("Hola")
    if(array.length>1){
      const index = parseInt(''+ (array.length/2-1));
      const p1 = mergeRec(array.slice(array[index], array.length))
      const p2 = mergeRec(array.slice(0, array.length/2))
      return merge(p1, p2)
    } else {
      return  array
    }
  }


  return mergeRec(array);
}

console.log(mergeSort([1,33,25,22,88,11,665,44,227,88,6321,31,1,32,3,52,1235,1,1,312,3423]))

// console.log("(GATO", "TOGA)","These words are anagrams ? :-", isAnagram("GATO", "TOGA"))
// console.log("(CALOR", "AMOR)","These words are anagrams ? :-", isAnagram("CALOR", "AMOR"))

// console.log("CommonElements on: [[1, 2, 3], ['1', 3, 'z', 3], [{caseName: 'word'}]]")
// console.log("Commons: ", findCommonElements([[1, 2, 3], ['1', 3, 'z', 3], [{caseName: 'word'}]]));
/*
console.log("Case  2")
console.log("Commons: ", findCommonElements([
  [1, 2, 3, []],
  ['1', 3, 'z', 3, []],
  [{caseName: 'word'}, '1', 3, 'z', 3],
  [[1, [], 'z', 3]]
]));*/
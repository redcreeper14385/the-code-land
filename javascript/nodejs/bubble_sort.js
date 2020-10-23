function bubbleSort(arr) {
    let inputLength = arr.length;
    let swapped;
    do {
      swapped = false;
      for (let i = 0; i < inputLength; i++) {
        if (arr[i] > arr[i + 1]) {
          let temp = arr[i];
          arr[i] = arr[i + 1];
          arr[i + 1] = temp;
          swapped = true;
        }
      }
    } while (swapped);
    return arr;
}
  
  const myArray = [0, 4, 22, 35, 25, 28, 67, 6, 9, 97, 85, 2, 1, 44]
  bubbleSort(myArray);
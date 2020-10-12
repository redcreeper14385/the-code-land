function insertionSort(arr) {
    let currentVal;
    for (let i = 1; i < arr.length; i++) {
        currentVal = arr[i];
        for (let j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = currentVal;
    }
    
    return arr;
}

const myArray = [0, 1, 29, 35, 9, 24, 16];
insertionSort(myArray);

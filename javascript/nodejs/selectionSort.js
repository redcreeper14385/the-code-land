function selectionSort(arr) {
    const swap = (arr, pos1, pos2) => ([arr[pos1], arr[pos2]] = [arr[pos2], arr[pos1]]);
    
    for (let i = 0; i < arr.length; i++) {
        let lowest = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[lowest] > arr[j]) {
                lowest = j;
            }
        }
        if (i !== lowest) swap(arr, i, lowest);
    }

    return arr;
}

const myArray = [0, 8, 21, 41, 55, 13, 17]
selectionSort(myArray);

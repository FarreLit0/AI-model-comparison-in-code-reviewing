function moveElementsToEndOfArray(arr, x) {

    let n = arr.length;
    x = x % n;

    let first_x_elements = arr.slice(0, x);

    let remaining_elements = arr.slice(x, n);


    arr = [...remaining_elements, ...first_x_elements];

    console.log(arr);
}

let arr = [1, 2, 3, 4, 5, 6];
let k = 5;

moveElementsToEndOfArray(arr, k);
function filteredArray(arr, elem) {
    let newArr = [...arr];

    for (let i = 0; i < newArr.length; i++) {
        let elemCheck = newArr[i].indexOf(elem);
        if (elemCheck != -1) {
            newArr.splice(i, 1);
        }
    }

    return newArr;
}


console.log(filteredArray([ ["trumpets", 2], ["flutes", 4], ["saxophones", 2] ], 2));


console.log(filteredArray([ ["amy", "beth", "sam"], ["dave", "sean", "peter"] ], "peter"));


console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));
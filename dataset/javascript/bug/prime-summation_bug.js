function primeSummation(n) {

    let vecOfPrimes = [2]
    let total = 0

    function isPrime(arr, number) {
        var result = arr.every(function(e) {
            return number % e
        });


        if (result == true) {
            arr.push(number)
        }
    }

    for (let i = 3; vecOfPrimes.length < 10001; i++) {
        isPrime(vecOfPrimes, i)

    }

    function isSmallEnough(value) {
        return value < n;
    }

    var filtered = vecOfPrimes.filter(isSmallEnough);

    for (let i = 0; i < filtered.length; i++) {
        total += filtered[i]
    }
    return total;
}

console.log(primeSummation(17)); // It should return 41
console.log(primeSummation(2001)); // It should return 277050
console.log(primeSummation(140759)); // It should return 873608362
console.log(primeSummation(2000000)); // It should return 142913828922
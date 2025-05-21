const random = () => {
    return Promise.resolve(Math.random())
}


const sumRandomAsyncNums = () => {
    let first;
    let second;
    let third;

    return random()
        .then(v => {
            first = v;
            return random();
        })
        .then(v => {
            second = v;
            return random();
        })
        .then(v => {
            third = v;
            return first + second + third
        })
        .then(v => {
            console.log(`Result ${v}`)
        });
}
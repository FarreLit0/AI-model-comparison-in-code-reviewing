
const random = () => {
    return Promise.resolve(Math.random())
}
const sumRandomAsyncNums = async() => {

    const first = await random();
    const second = await random();
    const third = await random();

    console.log(`Result ${first + second + third}`);

    if (await random()) {

    }

    const randos = Promise.all([
        random(),
        random(),
        random()
    ])

    for(const r of await randos) {
        console.log(r)
    }
}

sumRandomAsyncNums()

console.log('%c My Friends', 'color: orange; font-weight: bold;' )
console.log({ foo, bar, baz });

console.table([foo, bar, baz])

console.time('looper')

let i = 0;
while (i < 1000000) { i ++ }

console.timeEnd('looper')


const deleteMe = () => console.trace('bye bye database')

deleteMe()
deleteMe()
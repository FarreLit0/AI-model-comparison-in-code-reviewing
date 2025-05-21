// Computed Property Names

console.log('%c My Friends', 'color: orange; font-weight: bold;' )
console.log({ foo, bar, baz });

// Console.table(...)
console.table([foo, bar, baz])

// // Console.time
console.time('looper')

let i = 0;
while (i < 1000000) { i ++ }

console.timeEnd('looper')

// // Stack Trace Logs

const deleteMe = () => console.trace('bye bye database')

deleteMe()
deleteMe()
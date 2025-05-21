const turtle = {
    name: 'Bob',
    legs: 4,
    shell: true,
    type: 'amphibious',
    meal: 10,
    diet: 'berries'
}


function feed(animal) {
    return `Feed ${animal.name} ${animal.meal} kilos of ${animal.diet}`;
}
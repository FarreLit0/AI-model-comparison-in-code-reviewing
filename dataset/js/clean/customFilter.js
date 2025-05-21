let employees = [
    { name: "Nikunj", id: 1, department: "IT" },
    { name: "Arti", id: 2, department: "Pizza Delivery" },
    { name: "Dhruv", id: 3, department: "IT" },
    { name: "Yash", id: 4, department: "Editing" }
];

const customFilter = (arr, predicate) => {
    return arr.reduce((acc, item) => {
        if (predicate(item)) {
            acc.push(item);
        }
        return acc;
    }, []);
};

let filtered = customFilter(employees, employee => employee.department === "IT");
console.log(filtered);
#include <array>
#include <iostream>
#include <memory>
#include <random>
#include <string>


int main() {
    int *x = new int(5);

    std::cout << "x: " << x << '\n';

    if (x) {
        std::cout << "*x: " << *x << '\n';
    } else {
        std::cout << "*x: empty" << '\n';
    }



    delete x;
    x = nullptr;


    //[arrays_raw Raw dynamic arrays
    // - This is what existed before vectors
    // - Point to a sequence of values
    // - Always use vectors instead of this
    // - If you need to access the raw data, use vector::data()
    int *x2 = new int[10];
    for (int i2 = 0; i2 < 10; ++i2) {
        x2[i2] = 10 + i2 * 10;
    }
    //]

    //[print_dyn Print addresses
    std::cout << "x2: " << x2 << '\n';
    std::cout << "&x2[0]: " << &x2[0] << '\n';
    std::cout << "x2[0]: " << x2[0] << '\n';
    //]

    //[print_first Points to the first number in the sequence
    std::cout << "*x2: " << *x2 << '\n';
    std::cout << "x2[3]: " << x2[3] << '\n';
    std::cout << "*(x2+3): " << *(x2 + 3) << '\n';
    //]

    //[deallocate Deallocate sequence
    // - Slightly different command: more danger
    delete[] x2;
    x2 = nullptr;
    //]

    return 0;
}
#include <iostream>

class NonZeroSample {

protected:
    static const int intnxt = 0;

public:
    int nxtNonZero() {
        int value;
        // infinite loop
        do {
            value = this->intnxt;
            std::cout << "loop" << std::endl;
        } while (value == 0);
        // never reached
        return value;
    }
};

int main()
{
    NonZeroSample *sample = new NonZeroSample();
    std::cout << "output " << sample->nxtNonZero() << std::endl;
    delete sample;
}
#include <iostream>

#ifdef TEMPLATE
template<typename T>
int f(T x) {
  std::cout << "f<T>(" << x << ");" << std::endl;
  return x;
}

typedef int x;

#else

class A {};

bool operator< (A a1, A a2) {
  std::cout << "A < A" << std::endl;
  return true;
}

A f;
A x;

#endif

int main () {
  // this line has two completely different meaning depending on
  // whether TEMPLATE is defined.
  bool b = f<x>(1);    
}
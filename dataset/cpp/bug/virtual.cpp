#include <iostream>

/*
  This one is not too tricky, but this is just to illustrate the fact
  that you can't see wether a method is virtual just looking at the
  derived classes. Here, if you remove the function f in the Base
  class, this modifies the behavior of the fucntion f in the Derived
  class.
*/

using namespace std;

struct Base {
  virtual void f() {cout << "Base" << endl;}
};

struct Middle : public Base {
  void f() {cout << "Middle" << endl;}  
};

struct Derived : public Middle {
  void f() {cout << "Derived" << endl;}  
};

int main() {
  Base b;
  Middle m;
  Derived d;
  
  Middle * pb;
  pb = &m; pb->f();
  pb = &d; pb->f();
  
  return 0;
}
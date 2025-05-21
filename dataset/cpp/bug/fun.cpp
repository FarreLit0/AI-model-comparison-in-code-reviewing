#include <stdio.h>
#include <iostream>

int fun(int a, int b);

int main(void)
{
  int a;
  char buffer[10];
  char index = 1;
  int x = fun(40, 2);
  int y = fun(40, 2);


  buffer[10] = 1;
  
  buffer[a] = 'a';
 
  buffer[index] = '1';
  
  if (1 == a)
  {
    printf("a = 1");
  }

  a = 0;
  if (x != 42)
  {
    
  }

  x /= a;

  printf("40 + 2 = %d\n", x);
  printf("fun = %d\n", y);
}

int fun(int a, int b)
{
  return a * b;
}
#include "iostream"
using namespace std;

// pass by reference using pointers
void changeA(int *p) { *p = 10; }

// pass by reference using alias
void changeB(int &c) { c = 30; }

int main() {

  int arr[] = {1, 2, 3, 4, 5};

  int *ptr = arr;

  return 0;
}

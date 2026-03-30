#include <iostream>
#include <vector>
using namespace std;

void hanoi(int n, int source, int dest, int help) {
  if (n == 1) {
    cout << source << " -> " << dest << endl;
    return;
  } else {
    hanoi(n - 1, source, help, dest);
    cout << source << " -> " << dest << endl;
    hanoi(n - 1, help, dest, source);
  }
}

void towerhanoi(int n, int source, int help, int dest) {
  if (n == 1) {
    cout << source << " -> " << dest << endl;
    return;
  } else {
    towerhanoi(n - 1, source, dest, help);
    cout << source << " -> " << dest << endl;
    towerhanoi(n - 1, help, source, dest);
  }
}

int main() {
  // hanoi(3, 1, 3, 2);
  towerhanoi(3, 1, 2, 3);
  return 0;
}

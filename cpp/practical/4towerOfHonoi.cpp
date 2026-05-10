#include <iostream>
using namespace std;

void towerOfHonoi(int disks, int source, int helper, int destination) {
  if (disks == 1) {
    cout << "Move from tower " << source << " to " << destination << endl;
    return;
  } else {
    towerOfHonoi(disks - 1, source, destination, helper);
    cout << "Move disk from tower " << source << " to " << destination << endl;
    towerOfHonoi(disks - 1, helper, source, destination);
  }
}

int main() {
  towerOfHonoi(3, 1, 2, 3);
  return 0;
}

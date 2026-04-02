#include <iostream>
using namespace std;

double pow2(int x, int n) {
  // raise x to power n

  double ans = 1;
  int binForm = n;

  while (binForm > 0) {
    // if bit is set (ith bit)
    if (binForm & 1) {
      ans = ans * x;
    }
    x *= x;
    binForm = binForm >> 1;
  }

  return ans;
}

int main() {

  cout << pow2(3, 5) << endl;

  return 0;
}

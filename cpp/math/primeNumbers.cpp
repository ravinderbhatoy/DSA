#include <iostream>
#include <vector>
using namespace std;

int primeNumber(int n) {
  vector<int> isPrime{1, n + 1};
  for (auto it : isPrime)
    cout << it << " ";
  int count = 0;

  return count;
}

int main() {

  int n = primeNumber(10);
  cout << endl;

  return 0;
}

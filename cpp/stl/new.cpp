#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> arr = {1, 2, 2, 3, 4};

  auto itr = lower_bound(arr.begin(), arr.end(), 2);

  int ind = itr - arr.begin();
  cout << ind;

  return 0;
}

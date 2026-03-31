// https://www.naukri.com/code360/problems/bit-manipulation_8142533
#include <iostream>
#include <vector>
using namespace std;

vector<int> binManipulation(int n, int i) {
  i = i - 1 < 0 ? 0 : i - 1;
  vector<int> res;

  int bit = ((n >> i) & 1) != 0;

  res.push_back(bit);
  res.push_back((1 << i) | n);
  res.push_back(n & (~(1 << i)));
  return res;
}

int main() {

  vector<int> ans = binManipulation(9, 3);

  for (auto i : ans) {
    cout << i << " ";
  }
  cout << endl;

  return 0;
}

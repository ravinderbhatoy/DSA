#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int maxDepth(string s) {
  int maxCount = 0, count = 0;

  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '(')
      count++;
    if (s[i] == ')')
      count--;

    maxCount = max(count, maxCount);
  }
  return maxCount;
}

int main() {

  string s = "(1+(2*3)+((8)/4))+1";

  cout << maxDepth(s) << endl;
  return 0;
}

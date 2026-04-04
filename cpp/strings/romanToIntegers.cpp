#include <bits/stdc++.h>
using namespace std;

int getRomanValue(char c) {
  switch (c) {
  case 'I':
    return 1;
  case 'V':
    return 5;
  case 'X':
    return 10;
  case 'L':
    return 50;
  case 'C':
    return 100;
  case 'D':
    return 500;
  case 'M':
    return 1000;
  default:
    return 0;
  }
}

int romanToInt(string s) {
  int ans = 0;
  int prev = 0;

  for (int i = s.size() - 1; i >= 0; i--) {
    int value = getRomanValue(s[i]);
    if (value < prev)
      ans -= value;
    else
      ans += value;
    prev = value;
  }

  return ans;
}

int main() {
  string s = "III";
  cout << romanToInt(s) << endl;
  return 0;
}

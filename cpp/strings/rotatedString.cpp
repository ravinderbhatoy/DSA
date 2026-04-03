#include <bits/stdc++.h>
using namespace std;

bool rotatedString(string s, string goal) {
  if (s == goal)
    return true;
  // 1. bcdea -> cdeab -> deabc
  for (int i = 0; i < s.size(); i++) {
    char first = s[0];
    s.erase(0, 1);
    s += first;

    if (s == goal)
      return true;
  }
  return false;
}

int main() {

  string s = "abcde";
  string goal = "cdeab";

  return 0;
}

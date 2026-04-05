#include <bits/stdc++.h>
using namespace std;

string search(string &s, int left, int right) {

  int count = 0;

  while (left >= 0 && right < s.size() && s[left] == s[right]) {
    left--;
    right++;
  }
  return s.substr(left + 1, right - left - 1);
}

string longestPalindrome(string s) {
  string LPS = "";
  string ans = "";

  for (int i = 0; i < s.size(); i++) {
    // odd length comparison
    ans = search(s, i, i);
    if (ans.size() > LPS.size()) {
      LPS = ans;
    }
    // even
    ans = search(s, i, i + 1);
    if (ans.size() > LPS.size()) {
      LPS = ans;
    }
  }

  return LPS;
}

int main() {

  string s = "babad";
  cout << longestPalindrome(s) << endl;

  return 0;
}

#include <bits/stdc++.h>
using namespace std;

string reverseWords(string s) {
  int i = 0;
  int n = s.size();
  string ans = "";
  ans.reserve(n);

  // find end of words and reverse it

  reverse(s.begin(), s.end());
  while (i < n) {
    // skip spaces
    while (i < n && s[i] == ' ')
      i++;

    int start = i;
    // find end of word
    while (i < n && s[i] != ' ')
      i++;

    reverse(s.begin() + start, s.begin() + i);
    ans += s.substr(start, i - start);
    ans += ' ';
  }
  while (ans[ans.size() - 1] == ' ')
    ans.erase(ans.size() - 1);

  return ans;
}

int main() {

  string s = "  a good   morning     ";

  cout << reverseWords(s);

  return 0;
}

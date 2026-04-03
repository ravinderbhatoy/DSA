#include <bits/stdc++.h>
using namespace std;

string longestCommonPrefix(vector<string> &strs) {
  string ans;
  int n = strs.size();

  for (int i = 0; i < strs[0].size(); i++) {
    for (int j = 1; j < strs.size(); j++) {
      if (i >= strs[j].size()) {
        return ans;
      }
      if (strs[j][i] != strs[0][i]) {
        return ans;
      }
    }
    ans += strs[0][i];
  }
  return ans;
}

int main() {
  vector<string> strs = {"aa", "ab"};
  cout << longestCommonPrefix(strs);

  return 0;
}

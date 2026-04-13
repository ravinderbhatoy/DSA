#include <bits/stdc++.h>
using namespace std;

int lengthOfLongestSubstring(string s) {
  int maxLen = 0;
  int l = 0, r = 0;
  int n = s.size();

  vector<int> hash(256, -1);

  while (r < n) {
    if (hash[s[r]] >= l) {
      // update value in hash
      l = hash[s[r]] + 1;
    }
    // add to the hash
    hash[s[r]] = r;
    // calculate max length
    maxLen = max(r - l + 1, maxLen);
    r++;
  }

  return maxLen;
}

int main() {

  string s = " ";
  cout << lengthOfLongestSubstring(s);

  return 0;
}

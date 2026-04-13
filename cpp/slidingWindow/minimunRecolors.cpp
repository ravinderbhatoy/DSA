#include <bits/stdc++.h>
using namespace std;

int minimumRecolors(string blocks, int k) {
  int mini = INT_MAX;
  int n = blocks.size();
  int l = 0, r = 0, change = 0;
  while (r < n) {
    int len = r - l + 1;
    if (blocks[r] != 'B')
      change++;

    if (len > k) {
      if (blocks[l] == 'B')
        change--;
      l++;
    }
    len = r - l + 1;
    cout << len << "=" << r << "-" << l << "+" << 1 << endl;
    if (len == k && change >= 0) {
      mini = min(mini, change);
    }
    r++;
  }

  return mini;
}

int main() {

  string blocks = "BB";
  int k = 1;
  int change = minimumRecolors(blocks, k);
  cout << change << endl;

  return 0;
}

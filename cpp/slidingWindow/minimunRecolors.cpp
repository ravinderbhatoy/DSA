#include <bits/stdc++.h>
using namespace std;

int minimumRecolors(string blocks, int k) {
  int mini = k;
  int n = blocks.size();
  int l = 0, r = 0, change = 0;

  while (r < n) {
    if (blocks[r] != 'B')
      change++;

    if (r - l + 1 > k) {
      if (blocks[l] == 'W')
        change--;
      l++;
    }
    if (r - l + 1 > k) {
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

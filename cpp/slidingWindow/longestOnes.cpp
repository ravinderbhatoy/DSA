#include <bits/stdc++.h>
using namespace std;

int longestOnes(vector<int> &nums, int k) {
  int maxLen = 0, n = nums.size();
  int l = 0, r = 0, zeros = 0;

  while (r < n) {

    if (nums[r] == 0)
      zeros++;

    if (zeros > k) {
      if (nums[l] == 0)
        zeros--;
      l++;
    }

    if (zeros <= k) {
      maxLen = max(r - l + 1, maxLen);
    }

    r++;
  }

  return maxLen;
}

int main() {

  vector<int> nums = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
  int k = 2;

  cout << longestOnes(nums, k);

  return 0;
}

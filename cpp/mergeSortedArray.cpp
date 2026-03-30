#include <bits/stdc++.h>
using namespace std;

void mergeSorted(vector<int> &nums1, int m, vector<int> &nums2, int n) {
  int idx = m + n - 1;
  int i = m - 1;
  int j = n - 1;

  while (i >= 0 && j >= 0) {

    if (nums1[i] >= nums2[j]) {
      nums1[idx--] = nums1[i--];

    } else {
      nums1[idx--] = nums2[j--];
    }
  }

  while (j >= 0) {
    nums1[idx--] = nums2[j--];
  }
}

int main() {

  vector<int> nums1 = {4, 5, 6, 0, 0, 0};
  vector<int> nums2 = {2, 5, 6};

  mergeSorted(nums1, 3, nums2, 3);

  for (int ele : nums1) {
    cout << ele << " ";
  }

  return 0;
}

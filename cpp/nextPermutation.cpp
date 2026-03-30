#include "bits/stdc++.h"
#include <algorithm>
using namespace std;

void nextPermutation(vector<int> &nums) {

  // first find pivot element
  // pivot -> the element is < its right element starting from right
  // e.g [1,2,5,4,3] -> pivot -> 2 -> 2 < 5

  int n = nums.size();
  int i = n - 1;
  int pivotInd = 0;

  while (i > 0 && nums[i - 1] >= nums[i])
    i--;
  pivotInd = i - 1;

  if (pivotInd == -1) {
    // array is already in last permutation just reverse
    sort(nums.begin(), nums.end());
    return;
  }

  i = n - 1;
  int minLarInd = n - 1;

  while (i > pivotInd) {
    if (nums[i] > nums[pivotInd]) {
      minLarInd = i;
      break;
    }
    i--;
  }

  // swap pivot with next minimum largest
  swap(nums[pivotInd], nums[minLarInd]);
  sort(nums.begin() + pivotInd + 1, nums.end());
}

int main() {

  vector<int> nums = {2, 3, 1};

  nextPermutation(nums);

  for (int ele : nums) {
    cout << ele << " ";
  }

  return 0;
}

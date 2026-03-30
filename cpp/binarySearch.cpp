#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int> &nums, int target, int s, int e) {
  if (s > e) {
    return -1;
  }
  int mid = s + (e - s) / 2;
  if (nums[mid] > target) {
    return binarySearch(nums, target, s, mid - 1);
  } else if (nums[mid] < target) {
    return binarySearch(nums, target, mid + 1, e);
  } else {
    return mid;
  }
}

int main() {
  vector<int> nums = {-1, 0, 3, 5, 7, 9, 12};
  int target = -2;
  int start = 0;
  int end = nums.size() - 1;

  cout << binarySearch(nums, target, 0, end);

  return 0;
}

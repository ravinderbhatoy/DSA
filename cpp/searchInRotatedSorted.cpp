#include <iostream>
#include <vector>
using namespace std;

int bs(vector<int> &nums, int target) {

  int st = 0;
  int end = nums.size() - 1;

  while (st <= end) {
    int mid = st + (end - st) / 2;

    cout << "Mid: " << mid << endl;

    if (nums[mid] == target)
      return mid;

    if (nums[st] <= nums[mid]) {
      // checking if left half is sorted
      if (nums[st] <= target && target <= nums[mid]) {
        end = mid - 1;
      } else {
        st = mid + 1;
      }
    } else {
      // checking if right half is sorted
      if (nums[mid] <= target && target <= nums[end]) {
        st = mid + 1;
      } else {
        end = mid - 1;
      }
    }
  }

  return -1;
}

int main() {

  vector<int> nums = {7, 8, 0, 1, 2, 3, 4, 5};
  int target = 7;

  cout << bs(nums, target);

  // {3, 4, 5, 6, 7, 0, 1, 2};
  // ;

  return 0;
}

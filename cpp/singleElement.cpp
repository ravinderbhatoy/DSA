#include <iostream>
#include <vector>
using namespace std;

int singleElement(vector<int> &nums) {

  int size = nums.size();

  int st = 0;
  int end = size - 1;

  while (st <= end) {
    if (st == end)
      return nums[st];
    int mid = st + (end - st) / 2;
    if (mid > 0 && nums[mid - 1] == nums[mid]) {
      if (mid % 2 == 0)
        end = mid - 1;
      else
        st = mid + 1;
    } else if (nums[mid] == nums[mid + 1]) {
      if (mid % 2 == 0)
        st = mid + 1;
      else
        end = mid - 1;
    } else
      return nums[mid];
  }
  return -1;
}

int main() {

  vector<int> nums = {1, 1, 2, 2, 3};

  cout << singleElement(nums);

  return 0;
}

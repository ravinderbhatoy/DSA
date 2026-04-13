#include <iostream>
#include <vector>
using namespace std;

int peakIndex(vector<int> &nums) {
  int st = 1;
  int end = nums.size() - 2;

  while (st <= end) {

    int mid = st + (end - st) / 2;

    cout << "Mid: " << mid << endl;

    if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1])
      return mid;
    else if (nums[mid] > nums[mid + 1])
      end = mid - 1;
    else
      st = mid + 1;
  }

  return -1;
}

int main() {

  vector<int> nums = {3, 5, 3, 2, 0};

  cout << peakIndex(nums);

  return 0;
}

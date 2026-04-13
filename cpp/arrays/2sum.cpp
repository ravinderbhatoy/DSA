#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
  unordered_map<int, int> mp;

  for (int i = 0; i < nums.size(); i++) {
    int req = target - nums[i];
    if (mp.find(req) != mp.end()) {
      return {mp[req], i};
    } else {
      mp[nums[i]] = i;
    }
  }
  return {-1, -1};
}

int main() {

  vector<int> nums = {3, 2, 4};
  int target = 6;
  vector<int> ans = twoSum(nums, target);

  for (int ele : ans) {
    cout << ele << " ";
  }

  return 0;
}

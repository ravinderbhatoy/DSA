#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

void print_array(vector<int> &nums) {
  for (int i = 0; i < nums.size(); i++) {
    cout << nums[i] << " ";
  }
  cout << endl;
}

int get_digit(int number, int position) {
  while (position--)
    number /= 10;
  return number % 10;
}

void countSort(vector<int> &nums, int bit) {
  int size = nums.size();

  vector<int> freq(10, 0);
  for (int i = 0; i < size; i++) {
    freq[get_digit(nums[i], bit)]++;
  }

  vector<int> ans(size, 0);
  for (int i = 1; i < freq.size(); i++) {
    freq[i] += freq[i - 1];
  }

  for (int i = size - 1; i >= 0; i--) {
    ans[freq[get_digit(nums[i], bit)] - 1] = nums[i];
    freq[get_digit(nums[i], bit)]--;
  }

  nums = ans;
}

void radixSort(vector<int> &nums) {

  int size = nums.size();
  int maxi = *max_element(nums.begin(), nums.end());
  int mini = *min_element(nums.begin(), nums.end());

  // handling negative numbers
  if (mini < 0) {
    for (int i = 0; i < size; i++) {
      nums[i] = nums[i] - mini;
    }
  }
  print_array(nums);

  int bit = 0;
  while (maxi > 0) {
    countSort(nums, bit);
    maxi = maxi / 10;
    bit++;
  }

  if (mini < 0) {
    for (int i = 0; i < size; i++) {
      nums[i] = nums[i] + mini;
    }
  }
}

int main() {
  // vector<int> nums = {217, 98, 124, 1134, 375, 789, 419, -35, -45, -12};
  vector<int> nums = {-1, 2, 8, -10};
  radixSort(nums);
  print_array(nums);
  return 0;
}

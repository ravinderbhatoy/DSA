#include <bits/stdc++.h>
using namespace std;

int trapWater(vector<int> &height) {
  int n = height.size();
  int water = 0;
  int left = 0;
  int right = n - 1;

  int leftMax = height[left];
  int rightMax = height[right];

  while (left < right) {

    leftMax = max(height[left], leftMax);
    rightMax = max(height[right], rightMax);

    if (leftMax < rightMax) {
      water += leftMax - height[left];
      left++;
    } else {
      water += rightMax - height[right];
      right--;
    }
  }
  return water;
}

int main() {

  vector<int> height = {4, 2, 0, 3, 2, 5};
  cout << trapWater(height);
  cout << endl;

  return 0;
}

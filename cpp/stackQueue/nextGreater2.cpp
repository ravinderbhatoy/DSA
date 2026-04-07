#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreater(vector<int> &nums) {
  int n = nums.size();
  stack<int> st;
  vector<int> ans(n);

  for (int i = 2 * n - 1; i >= 0; i--) {
    while (!st.empty() && st.top() <= nums[i % n]) {
      st.pop();
    }
    if (i < n) {
      ans[i] = st.empty() ? -1 : st.top();
    }
    st.push(nums[i % n]);
  }

  return ans;
}

int main() {

  vector<int> nums = {1, 2, 3, 4, 3};

  vector<int> ans = nextGreater(nums);

  for (auto ele : ans)
    cout << ele << " ";
  cout << endl;

  return 0;
}

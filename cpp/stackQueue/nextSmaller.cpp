#include <bits/stdc++.h>
using namespace std;

vector<int> nextSmaller(vector<int> nums) {
  int n = nums.size();
  vector<int> ans(n, -1);
  stack<int> st;

  for (int i = n - 1; i >= 0; i--) {
    while (!st.empty() and st.top() >= nums[i]) {
      st.pop();
    }

    if (!st.empty()) {
      ans[i] = st.top();
    }
    st.push(nums[i]);
  }
  return ans;
}

int main() {
  vector<int> nums = {1, 3, 2, 4};
  vector<int> ans = nextSmaller(nums);
  for (auto ele : ans)
    cout << ele << " ";
  cout << endl;

  return 0;
}

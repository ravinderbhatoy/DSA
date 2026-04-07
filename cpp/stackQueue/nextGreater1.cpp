#include <bits/stdc++.h>
using namespace std;

vector<int> nextGreater(vector<int> &nums1, vector<int> &nums2) {
  int n = nums2.size();
  int m = nums1.size();
  vector<int> ans(m);
  unordered_map<int, int> umap;

  stack<int> st;

  for (int i = n - 1; i >= 0; i--) {
    while (!st.empty() && st.top() <= nums2[i]) {
      st.pop();
    }
    if (st.empty()) {
      umap[nums2[i]] = -1;
    } else {
      umap[nums2[i]] = st.top();
    }
    st.push(nums2[i]);
  }

  for (int i = 0; i < m; i++) {
    ans[i] = umap[nums1[i]];
  }

  return ans;
}

int main() {

  vector<int> nums1 = {4, 1, 2};
  vector<int> nums2 = {1, 3, 4, 2};

  vector<int> ans = nextGreater(nums1, nums2);

  for (auto ele : ans)
    cout << ele << " ";
  cout << endl;

  return 0;
}

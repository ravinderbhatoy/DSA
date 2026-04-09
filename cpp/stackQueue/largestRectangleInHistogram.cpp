#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int> &heights) {
  int n = heights.size();
  stack<int> st;
  int maxArea = 0;

  for (int i = 0; i < n; i++) {
    while (!st.empty() && heights[st.top()] >= heights[i]) {
      int ind = st.top();
      st.pop();
      int nse = i;
      int pse = st.empty() ? -1 : st.top();
      maxArea = max(maxArea, heights[ind] * (nse - pse - 1));
    }
    st.push(i);
  }

  while (!st.empty()) {
    int nse = n;
    int ind = st.top();
    st.pop();
    int pse = st.empty() ? -1 : st.top();
    maxArea = max(maxArea, heights[ind] * (nse - pse - 1));
  }
  return maxArea;
}

int main() {

  vector<int> heights = {2, 1, 5, 6, 2, 3};
  cout << largestRectangleArea(heights);

  return 0;
}

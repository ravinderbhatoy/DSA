#include <bits/stdc++.h>
using namespace std;

vector<int> findNSE(vector<int> arr) {
  int n = arr.size();
  vector<int> ans(n, n);
  stack<int> st;

  for (int i = n - 1; i >= 0; i--) {
    while (!st.empty() && arr[st.top()] >= arr[i]) {
      st.pop();
    }
    if (!st.empty()) {
      ans[i] = st.top();
    }
    st.push(i);
  }
  return ans;
}

vector<int> findPSEE(vector<int> arr) {
  int n = arr.size();
  vector<int> ans(n, -1);
  stack<int> st;

  for (int i = 0; i < n; i++) {
    while (!st.empty() && arr[st.top()] > arr[i]) {
      st.pop();
    }
    if (!st.empty()) {
      ans[i] = st.top();
    }
    st.push(i);
  }
  return ans;
}

int sumOfSubarraMin(vector<int> arr) {
  vector<int> nse = findNSE(arr);
  // previous smaller or equal element
  vector<int> pse = findPSEE(arr);
  int sum = 0;
  int mod = 1e9 + 7;

  for (int i = 0; i < arr.size(); i++) {
    int left = i - pse[i];
    int right = nse[i] - i;

    long long freq = right * left * 1LL;
    int val = (freq * arr[i] * 1LL) % mod;
    sum = (sum + val) % mod;
  }
  return sum;
}

int main() {

  vector<int> arr = {3, 1, 2, 4};
  vector<int> sub;
  cout << sumOfSubarraMin(arr);

  return 0;
}

// Breaking Down the Logic
// 1. Range of Influence
//
// For any element arr[i], we need to find the largest window (pse[i], nse[i])
// where arr[i] remains the smallest value.
//
//     left: The distance to the Previous Smaller or Equal Element. This
//     represents how many starting positions to the left (including i itself)
//     can form a subarray where arr[i] is the minimum.
//
//     right: The distance to the Next Smaller Element. This represents how many
//     ending positions to the right (including i itself) can form a subarray
//     where arr[i] is the minimum.
//
// 2. The Combinatorics
//
// The number of subarrays where arr[i] is the minimum is calculated as:
// Total Subarrays=left×right
//
//     Note on the "Equal" part: > You used findPSEE (Previous Smaller or Equal)
//     for the left side and findNSE (Next Smaller) for the right. This is a
//     crucial detail! It prevents double-counting subarrays that contain
//     duplicate minimum values (e.g., in [2, 3, 2], one 2 handles the "equal
//     to" cases while the other doesn't).
//
// 3. Contribution Calculation
//
//     freq: The number of subarrays where arr[i] is the boss.
//
//     val: The total value contributed by arr[i] to the final sum (freq×value).
//
//     Modulo: The use of 1LL ensures the multiplication is handled in long long
//     to prevent overflow before the modulo operation.
//
// Dry Run Example
//
// If arr = [3, 1, 2, 4]:
//
//     For 1 at index 1:
//
//         pse[1] = -1 (no smaller to the left), so left = 1 - (-1) = 2.
//
//         nse[1] = 4 (no smaller to the right), so right = 4 - 1 = 3.
//
//         freq = 2 * 3 = 6.
//
//         Subarrays: [1], [3,1], [1,2], [1,2,4], [3,1,2], [3,1,2,4]. All have 1
//         as the minimum.

#include <bits/stdc++.h>
using namespace std;

int getMin(int arr[26]) {
  int mini = INT_MAX;
  for (int i = 0; i < 26; i++) {
    if (arr[i] != 0) {
      mini = min(arr[i], mini);
    }
  }
  return mini;
}

int getMax(int arr[26]) {
  int maxi = 0;
  for (int i = 0; i < 26; i++) {
    maxi = max(arr[i], maxi);
  }
  return maxi;
}

int beautySum(string s) {
  int sum = 0;
  for (int i = 0; i < s.size(); i++) {
    int freq[26] = {0};

    for (int j = i; j < s.size(); j++) {
      freq[s[j] - 'a']++;
      int mini = getMin(freq);
      int beauty = mini > 0 ? getMax(freq) - mini : 0;
      sum += beauty;
    }
  }
  return sum;
}

int main() {

  string s = "aabcb";
  cout << beautySum(s) << endl;
}

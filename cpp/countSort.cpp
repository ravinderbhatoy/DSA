#include <bits/stdc++.h>
using namespace std;
void print_array(vector<int> &arr) {
  for (int i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

void countSort(vector<int> &arr) {
  int maxi = arr[0];
  int size = arr.size();
  for (auto it : arr) {
    maxi = max(it, maxi);
  }

  // count frequency of each element
  vector<int> freq(maxi + 1, 0);
  for (int i = 0; i < size; i++) {
    freq[arr[i]]++;
  }

  // computer prefix sum
  vector<int> ans(size, 0);
  for (int i = 1; i < freq.size(); i++) {
    freq[i] += freq[i - 1];
  }

  // placement
  for (int i = size - 1; i >= 0; i--) {
    ans[freq[arr[i]] - 1] = arr[i];
    freq[arr[i]]--;
  }
  // copy elements
  for (int i = 0; i < size; i++) {
    arr[i] = ans[i];
  }
}

int main() {
  vector<int> arr = {2, 2, 0, 3, 5, 4, 1};
  countSort(arr);
  print_array(arr);

  return 0;
}

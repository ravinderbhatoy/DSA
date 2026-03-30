#include <iostream>
using namespace std;
int linearSearch(int arr[], int n, int target) {
  for (int i = 0; i < n; i++) {
    if (arr[i] == target)
      return i;
  }
  return -1;
}
int main() {
  int size = 5, target, arr[size];
  cout << "Insert 5 elements in array: \n";
  for (int i = 0; i < size; i++) {
    cin >> arr[i];
  }
  cout << "Insert element to be found: ";
  cin >> target;
  int ans = linearSearch(arr, size, target);
  if (ans < 0) {
    cout << "Element not found\n";
  } else {
    cout << "Element is at index: " << ans << endl;
  }
  return 0;
}

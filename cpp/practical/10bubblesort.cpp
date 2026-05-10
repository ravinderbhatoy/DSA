#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
  // place elements at the end (correct position)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      // keep comparing two adjacent elements
      if (arr[j] > arr[j + 1]) {
        // swap if order is incorrect
        swap(arr[j], arr[j + 1]);
      }
    }
  }
}

int main() {

  int arr[] = {30, 20, 10, 5, 50};
  int n = 5;

  bubbleSort(arr, n);

  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}

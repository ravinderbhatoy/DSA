#include <iostream>
using namespace std;

void insertSort(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    int key = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > key) {
      // shift elements one position ahead
      arr[j + 1] = arr[j];
      j--;
    }
    // original element
    arr[j + 1] = key;
  }
}

int main() {
  int arr[] = {10, 5, 30, 20, 50};
  int n = 5;

  insertSort(arr, n);

  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}

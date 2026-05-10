#include <iostream>
using namespace std;

void selectionSort(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    int sm = i;
    for (int j = i; j < n; j++) {
      if (arr[j] < arr[sm]) {
        sm = j;
      }
    }
    swap(arr[i], arr[sm]);
  }
}

int main() {

  int arr[] = {10, 5, 30, 20, 50};
  int n = 5;
  selectionSort(arr, n);

  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}

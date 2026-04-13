#include <iostream>
using namespace std;
void printArray(int arr[], int n) {
  cout << "{ ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << "}" << endl;
}
int main() {

  int arr[50], choice, element;
  int current_size = 5;

  cout << "Enter any five elements: " << endl;
  for (int i = 0; i < current_size; i++) {
    cin >> arr[i];
  }
  printArray(arr, current_size);

  cout << "Enter choice insert or delete (1 or 2): ";
  cin >> choice;

  if (choice == 1) {
    cout << "Enter the element to insert: ";
    cin >> element;
    arr[current_size++] = element;
    cout << "Array after inserting the element" << endl;
    printArray(arr, current_size);
  } else if (choice == 2) {
    cout << "Enter element to delete: ";
    cin >> element;
    int i = 0;
    for (; i < current_size; i++) {
      if (arr[i] == element) {
        break;
      }
    }
    int start = i;
    while (start < current_size) {
      arr[start++] = arr[start + 1];
    }
    current_size--;

    cout << "Array after deleting the element" << endl;
    printArray(arr, current_size);
  } else {
    cout << "Invalid input" << endl;
  }

  return 0;
}

#include <iostream>
#include <vector>
using namespace std;

vector<int> aestroids(vector<int> arr) {
  vector<int> survivors;

  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > 0) {
      survivors.push_back(arr[i]);
    } else {
      while (survivors.size() > 0) {
        int top = survivors[survivors.size() - 1];
        if (top < abs(arr[i])) {
          survivors.pop_back();
        } else {
          break;
        }
      }
    }
    if (survivors.size() == 0) {
      survivors.push_back(arr[i]);
    }
  }

  return survivors;
}

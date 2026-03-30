#include <iostream>
using namespace std;

class que {
private:
  const static int size = 10;
  int arr[size];
  int start, end = -1;
  int curr_size = 0;

public:
  void push(int val) {
    if (curr_size == size) {
      cout << "Overflow\n";
      return;
    }
    if (curr_size == 0) {
      start = 0, end = 0;
    } else {
      // will fill empty spaces on front
      end = (end + 1) % size;
    }
    arr[end] = val;
    curr_size += 1;
  }

  int pop() {
    if (curr_size == 0) {
      return -1;
    }

    int ele = arr[start];

    if (curr_size == 1) {
      start = end = -1;
    }

    start = (start + 1) % size;
    curr_size -= 1;
    return ele;
  }

  int top() { return (curr_size == 0) ? -1 : arr[start]; }

  int length() { return curr_size; }
};

int main() {

  que q;
  q.push(10);
  q.push(20);
  q.push(30);
  q.push(40);

  q.pop();
  cout << q.top() << endl;

  return 0;
}

#include <iostream>
using namespace std;

const int maxSize = 5;
int arr[maxSize];

class Stack {
private:
  int top = -1;

public:
  void push(int val) {
    if (top == maxSize - 1) {
      cout << "Overflow" << endl;
    } else {
      top++;
      arr[top] = val;
    }
  }

  void pop() {
    if (top == -1) {
      cout << "Underflow" << endl;
    } else {
      top--;
    }
  }

  int peak() {
    if (top == -1) {
      cout << "Underflow";
      return -1;
    }
    return arr[top];
  }
};

int main() {

  Stack st;
  st.push(100);
  st.push(200);
  st.push(300);
  st.push(400);
  st.push(500);
  st.push(600);

  cout << st.peak() << endl;
  cout << st.peak() << endl;

  st.pop();
  cout << st.peak() << endl;
  st.pop();
  cout << st.peak() << endl;

  return 0;
}

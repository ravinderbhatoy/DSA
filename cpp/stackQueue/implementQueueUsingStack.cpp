#include <bits/stdc++.h>
#include <stack>
using namespace std;

class MyQueue {
  // two stacks
  stack<int> st1;
  stack<int> st2;

public:
  void push(int x) {
    // empty stack 1
    while (!st1.empty()) {
      st2.push(st1.top());
      st1.pop();
    }
    // push data to stack 1
    st1.push(x);

    // push data again to stack 1 from stack 2
    while (!st2.empty()) {
      st1.push(st2.top());
      st2.pop();
    }
  }
  int pop() {
    int last = st1.top();
    st1.pop();
    return last;
  }
  int peek() { return st1.top(); }
  bool empty() { return st1.empty(); }
};

int main() { return 0; }

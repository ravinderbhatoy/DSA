#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

class MyStack {

  queue<int> que;

public:
  void push(int x) {
    int size = que.size();
    que.push(x);

    for (int i = 0; i < size; i++) {
      que.push(que.front());
      que.pop();
    }
  }
  int pop() {
    int front = que.front();
    que.pop();
    return front;
  }

  int top() { return que.front(); }

  bool empty() { return que.empty(); }
};

int main() {

  MyStack st;
  st.push(4);
  st.push(9);
  st.push(2);
  st.push(5);

  cout << st.top() << endl;

  return 0;
}

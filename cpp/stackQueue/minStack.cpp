#include <bits/stdc++.h>
using namespace std;

class MinStack {
  stack<int> st;
  stack<int> preMins;

public:
  void push(int x) {
    st.push(x);
    if (!preMins.empty() && preMins.top() < x) {
      preMins.push(preMins.top());
    } else {
      preMins.push(x);
    }
  }

  void pop() {
    st.pop();
    preMins.pop();
  }

  int top() { return st.top(); }

  int getMin() { return preMins.top(); }
};

int main() {
  MinStack ms;
  ms.push(10);
  ms.push(5);
  ms.push(1);

  cout << ms.getMin() << endl;
  ms.pop();
  cout << ms.getMin() << endl;
  ms.pop();
  cout << ms.getMin() << endl;
  ms.pop();

  ms.push(-2);
  ms.push(-1);
  ms.push(-2);

  cout << ms.getMin();

  return 0;
}

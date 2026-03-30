#include <iostream>
#include <stack>
using namespace std;

class queueWstack {
  stack<int> s1;
  stack<int> s2;

public:
  void push(int val) {
    // move s1 elements to s2 (s1 -> s2)
    while (!s1.empty()) {
      s2.push(s1.top());
      s1.pop();
    }
    // add new element to s1
    s1.push(val);
    // move all element again from s2 -> s1
    while (!s2.empty()) {
      s1.push(s2.top());
      s2.pop();
    }
  }

  int pop() {
    int res = s1.top();
    s1.pop();
    return res;
  }

  int top() { return s1.top(); }
};

int main() {

  queueWstack q;
  q.push(10);
  q.push(20);
  q.push(30);

  return 0;
}

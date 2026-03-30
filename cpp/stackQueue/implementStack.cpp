#include <iostream>
using namespace std;

class stImpl {
  int topEle = -1;
  const static int capacity = 10;
  int st[capacity];

public:
  void push(int value) {
    if (topEle >= capacity - 1) {
      cout << "Overflow\n";
      return;
    }
    topEle++;
    st[topEle] = value;
  }

  int top() {
    if (topEle == -1) {
      return -1;
    }
    return st[topEle];
  }

  void pop() {
    if (topEle == -1) {
    } else {
      topEle--;
    }
  }

  int size() { return topEle + 1; }
};

int main() {
  stImpl st;
  st.push(10);
  st.push(20);
  st.push(30);
  st.push(40);
  st.push(50);
  st.push(60);
  st.push(70);
  st.push(80);
  st.push(90);
  st.push(100);
  st.push(100);
  cout << st.size();

  return 0;
}

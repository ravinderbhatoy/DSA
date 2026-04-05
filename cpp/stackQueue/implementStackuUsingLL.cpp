#include <bits/stdc++.h>
using namespace std;

struct Node {
  Node *next;
  int data;

  Node(int data1) {
    data = data1;
    next = nullptr;
  }

  Node(int data1, Node *next1) {
    data = data1;
    next = next1;
  }
};

class StackLL {
  Node *head = nullptr;

public:
  void push(int data) { head = new Node(data, head); }

  int pop() {

    if (head == nullptr)
      return -1;

    Node *temp = head;
    head = head->next;
    int data = temp->data;
    delete temp;
    return data;
  }

  int top() { return head != nullptr ? head->data : -1; }
};

int main() {

  StackLL stack;
  stack.push(10);
  stack.push(20);
  stack.push(30);

  cout << stack.top() << endl;

  return 0;
}

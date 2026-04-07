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
  int size = 0;

public:
  void push(int data) {
    head = new Node(data, head);
    size++;
  }

  int pop() {

    if (head == nullptr)
      return -1;
    Node *temp = head;
    head = head->next;
    int data = temp->data;
    delete temp;
    size--;
    return data;
  }

  int top() { return head != nullptr ? head->data : -1; }
  int getSize() { return size; }
};

int main() {

  StackLL stack;
  stack.push(10);
  stack.push(20);
  stack.push(30);

  cout << stack.pop() << endl;
  cout << stack.pop() << endl;
  cout << stack.pop() << endl;
  cout << stack.getSize() << endl;

  stack.push(30);
  cout << stack.getSize() << endl;

  return 0;
}

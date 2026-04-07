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

class queueLL {
  Node *head = nullptr;
  Node *tail = nullptr;
  int size = 0;

public:
  void push(int data) {
    Node *newNode = new Node(data);
    if (head == nullptr) {
      head = tail = newNode;
    } else {
      tail->next = newNode;
      tail = newNode;
    }
    size++;
  }

  int pop() {
    if (head == nullptr)
      return -1;

    Node *temp = head;
    head = head->next;

    if (head == nullptr) {
      head = tail = nullptr;
    }

    int value = temp->data;
    delete temp;
    size--;

    return value;
  }

  int top() { return head == nullptr ? -1 : head->data; }

  int getSize() { return size; }
};

int main() {

  queueLL que;
  que.push(7);
  que.push(2);
  que.push(3);
  que.push(5);

  cout << que.top() << endl;
  cout << que.getSize() << endl;

  cout << que.pop() << endl;
  cout << que.pop() << endl;
  cout << que.pop() << endl;
  cout << que.pop() << endl;
  cout << que.pop() << endl;

  cout << que.getSize() << endl;

  return 0;
}

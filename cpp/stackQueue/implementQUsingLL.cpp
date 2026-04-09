#include <iostream>
using namespace std;

struct Node {
  Node *next;
  int data;

  Node(int data1) {
    data = data1;
    next = nullptr;
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

  void show() {
    if (head == nullptr)
      return;
    Node *temp = head;
    while (temp != nullptr) {
      cout << temp->data << "->";
      temp = temp->next;
    }
    cout << endl;
  }
};

int main() {

  queueLL que;
  cout << "Pushing 7: " << endl;
  que.push(7);
  cout << "Pushing 2: " << endl;
  que.push(2);
  cout << "Pushing 3: " << endl;
  que.push(3);
  cout << "Pushing 5: " << endl;
  que.push(5);
  cout << "Popping out" << endl;
  que.pop();
  cout << "Popping out" << endl;
  que.pop();

  cout << "Size of Queue: " << que.getSize() << endl;
  cout << "Top of Queue: " << que.top() << endl;
  cout << "Printing queue: " << endl;
  que.show();

  return 0;
}

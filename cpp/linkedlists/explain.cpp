#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *next; // address(pointer)

  Node(int data1) {
    data = data1;
    next = nullptr;
  }
};

Node *insert_front(Node *head, int value) {
  Node *newNode = new Node(value);
  if (head == nullptr) {
    head = newNode;
  } else {
    newNode->next = head;
    head = newNode;
  }
  return head;
}

Node *insert_end(Node *head, int value) {
  Node *newNode = new Node(value);
  if (head == nullptr) {
    head = newNode;
  } else {
    Node *temp = head;
    while (temp->next != nullptr) {
      temp = temp->next;
    }
    temp->next = newNode;
  }
  return head;
}

Node *delete_front(Node *head) {
  if (head == nullptr) {
    cout << "underflow" << endl;
  } else {
    Node *preHead = head;
    head = head->next;
    delete preHead;
  }
  return head;
}

Node *delete_end(Node *head) {
  if (head == nullptr) {
    cout << "Underflow" << endl;
    return head;
  } else {
    Node *temp = head;
    while (temp->next && temp->next->next != nullptr) {
      temp = temp->next;
    }
    temp->next = nullptr;
  }
  return head;
}

int main() {
  Node *head = new Node(10);
  head = insert_front(head, 20);
  head = insert_front(head, 30);
  head = insert_front(head, 40);
  head = insert_end(head, 50);
  head = insert_end(head, 60);
  // 40 -> 30 -> 20 -> 10 -> 50 -> 60
  head = delete_front(head);
  // 30 -> 20 -> 10 -> 50 -> 60
  head = delete_front(head);
  // 20 -> 10 -> 50 -> 60
  head = delete_end(head);
  // 20 -> 10 -> 50
  head = delete_end(head);
  // 20 -> 10 ->
  Node *temp = head;

  while (temp != nullptr) {
    cout << temp->data << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;

  return 0;
}

#include <iostream>
using namespace std;

// custom data type to store (data & pointer(next data location))
class Node {
public:
  int data;
  Node *next;

  Node(int val) {
    data = val;
    next = NULL;
  }
};

// List will store all nodes (for traversing)
class List {
  Node *head;
  Node *tail;

public:
  // initialize as empty
  List() { head = tail = NULL; }

  void printLL() {
    Node *temp = head;
    while (temp != NULL) {
      cout << temp->data << "->";
      temp = temp->next;
    }
    cout << "NULL" << endl;
  }

  void push_front(int val) {
    Node *newNode = new Node(val);
    if (head == NULL) {
      // on empty list
      head = tail = newNode;
    } else {
      newNode->next = head;
      head = newNode;
    }
  }

  void push_back(int val) {
    Node *newNode = new Node(val);
    if (head == NULL) {
      head = tail = newNode;
    } else {
      tail->next = newNode;
      tail = newNode;
    }
  }

  void insert(int pos, int val) {
    if (pos < 0) {
      cout << "Invalid position\n";
      return;
    }
    if (pos == 0) {
      push_front(val);
      return;
    }

    int cnt = 0;
    Node *temp = head;
    while (cnt < pos - 1 && temp != NULL) {
      temp = temp->next;
      cnt++;
    }
    if (temp != NULL) {
      Node *newNode = new Node(val);
      newNode->next = temp->next;
      temp->next = newNode;
    } else {
      cout << "Invalid position \n";
    }
  }

  void pop_front() {
    if (head == NULL) {
      cout << "LL is empty\n";
    } else {
      Node *temp = head;
      head = head->next;
      delete temp;
    }
  }

  void pop_back() {
    if (head == NULL) {
      cout << "LL is empty\n";
    } else {
      Node *temp = head;
      // find node before tail
      while (temp->next != tail) {
        temp = temp->next;
      }
      temp->next = NULL;
      delete tail;
      tail = temp;
    }
  }

  int find(int key) {
    Node *temp = head;
    int idx = 0;
    while (temp != NULL) {
      if (temp->data == key) {
        return idx;
      }
      temp = temp->next;
      idx++;
    }
    return -1;
  }

  void reverseLL() {
    if (head == NULL || head->next == NULL) {
      return;
    } else if (head == tail) {
      // only single element is there
      return;
    }
    Node *prev = NULL;
    Node *curr = head;
    Node *next = NULL;

    while (curr != NULL) {
      next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }
    tail = head;
    head = prev;
  }

  void removeCycle() {
    Node *slow, *fast = head;
    bool hasCycle = false;
    // check if cycle exist
    while (fast != NULL and fast->next != NULL) {
      slow = slow->next;
      fast = fast->next->next;

      if (slow == fast) {
        hasCycle = true;
        break;
      }
    }

    if (!hasCycle)
      return;
    slow = head;
    Node *prev = NULL;
    while (slow != fast) {
      slow = slow->next;
      prev = fast;
      fast = fast->next;
    }
    // remove cycle
    prev->next = NULL;
    return;
  }
};

int main() {
  List ll;
  ll.push_back(10);
  ll.push_back(20);
  ll.push_back(30);

  ll.printLL();
  ll.reverseLL();
  ll.printLL();

  ll.push_front(40);
  ll.push_back(50);
  ll.reverseLL();
  ll.printLL();

  return 0;
}

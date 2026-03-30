#include <bits/stdc++.h>
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
  // call default constructor first
  List(vector<int> &arr) : List() {
    for (int i = 0; i < arr.size(); i++) {
      this->push_back(arr[i]);
    }
  }

  void printLL() {
    Node *temp = head;
    cout << "Head->";
    while (temp != NULL) {
      cout << temp->data << " ";
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
      if (head == NULL)
        tail = NULL;
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

  void remove(int val) {
    if (head == NULL) {
      return;
    }
    Node *curr = head;
    Node *prev = NULL;

    while (curr != NULL) {
      if (curr->data == val) {
        // Case1: Removing head
        if (prev == NULL) {
          head = curr->next;
          if (head == NULL)
            tail = NULL;
        } else {
          prev->next = curr->next;
          if (curr == tail)
            tail = prev;
        }
        delete curr;
        return;
      }
      prev = curr;
      curr = curr->next;
    }
  }

  int middleNode() {
    Node *slow = head;
    Node *fast = head;
    while (fast != NULL && fast->next != NULL) {
      slow = slow->next;
      fast = fast->next->next;
    }
    return slow->data;
  }
};

Node *convertToLL(vector<int> &arr) {
  Node *head = new Node(arr[0]);
  Node *mover = head;
  for (int i = 1; i < arr.size(); i++) {
    Node *temp = new Node(arr[i]);
    mover->next = temp;
    mover = temp;
  }
  return head;
}

void printLL(Node *head) {
  Node *temp = head;
  cout << "Head->";
  while (temp != NULL) {
    cout << temp->data << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;
}

int main() {
  vector<int> arr = {1, 2, 3, 3, 4, 6, 8};
  List ll(arr);
  for (auto it : arr) {
    ll.remove(it);
  }
  ll.printLL();
  return 0;
}

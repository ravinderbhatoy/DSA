#include <bits/stdc++.h>
using namespace std;

struct Node {
public:
  int data;
  Node *next;
  // doubly connection
  Node *back;

public:
  Node(int data1) {
    data = data1;
    next = NULL;
    back = NULL;
  }

  Node(int data1, Node *next1) {
    data = data1;
    next = next1;
    back = NULL;
  }

  Node(int data1, Node *next1, Node *back1) {
    data = data1;
    next = next1;
    back = back1;
  }
};

Node *convert2DLL(vector<int> &arr) {
  Node *head = new Node(arr[0]);
  Node *prev = head;
  for (int i = 1; i < arr.size(); i++) {
    Node *temp = new Node(arr[i], NULL, prev);
    prev->next = temp;
    prev = temp;
  }
  return head;
}

Node *removeHead(Node *head) {
  if (head == NULL) {
    return NULL;
  }
  Node *temp = head;
  head = head->next;
  if (head != NULL) {
    head->back = NULL;
  }
  delete temp;
  return head;
}

Node *removeTail(Node *head) {
  if (head == NULL) {
    return NULL;
  }
  if (head->next == NULL) {
    delete head;
    return NULL;
  }
  Node *temp = head;
  while (temp->next != NULL) {
    temp = temp->next;
  }
  temp->back->next = NULL;
  delete temp;
  return head;
}

Node *removeAt(Node *head, int pos) {
  if (head == NULL || pos < 0)
    return NULL;
  // remove head
  if (pos == 0) {
    return removeHead(head);
  }
  int cnt = 0;
  Node *temp = head;
  while (cnt != pos && temp != NULL) {
    temp = temp->next;
    cnt++;
  }
  // position is not out of range
  if (temp != NULL) {
    Node *prev = temp->back;
    Node *next = temp->next;
    // removing tail
    if (next == NULL) {
      return removeTail(head);
    }
    prev->next = next;
    next->back = prev;
    delete temp;
  }
  return head;
}

Node *removeValue(Node *head, int target) {
  // LL is empty
  if (head == NULL)
    return NULL;
  // removing head
  if (head->data == target)
    return removeHead(head);

  Node *temp = head;
  while (temp != NULL && temp->data != target) {
    temp = temp->next;
  }
  // target doesn't exist
  if (temp == NULL)
    return head;

  Node *prev = temp->back;
  Node *next = temp->next;

  // removing tail
  if (next == NULL) {
    prev->next = NULL;
    delete temp;
    return head;
  }

  prev->next = next;
  next->back = prev;
  delete temp;
  return head;
}

void deleteNode(Node *temp) {
  Node *prev = temp->back;
  Node *next = temp->next;

  if (next == NULL) {
    prev->next = NULL;
    delete temp;
    return;
  }
  prev->next = next;
  next->back = prev;
  delete temp;
}

Node *insertBeforeHead(Node *head, int value) {
  Node *newHead = new Node(value, head);
  head->back = newHead;
  return newHead;
}

Node *insertBeforeTail(Node *head, int value) {
  // find tail
  Node *tail = head;
  while (tail->next != NULL) {
    tail = tail->next;
  }
  if (tail->back == NULL) {
    return insertBeforeHead(head, value);
  }
  Node *prev = tail->back;
  Node *temp = new Node(value, tail, prev);
  prev->next = temp;
  tail->back = temp;
  return head;
}

Node *insertBeforePos(Node *head, int pos, int value) {
  if (head == NULL || pos < 0)
    return head;

  if (pos == 0)
    return insertBeforeHead(head, value);

  int cnt = 0;
  Node *temp = head;

  while (temp != NULL && cnt != pos) {
    cnt++;
    temp = temp->next;
  }

  if (temp == NULL) {
    return head;
  }

  Node *prev = temp->back;
  Node *newNode = new Node(value, temp, prev);
  prev->next = newNode;
  temp->back = newNode;
  return head;
}

void insertBefore(Node *temp, int value) {
  Node *prev = temp->back;
  Node *newNode = new Node(value, temp, prev);
  prev->next = newNode;
  temp->back = newNode;
}

void print(Node *head) {
  Node *temp = head;
  while (temp != NULL) {
    cout << temp->data << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;
}

void printRev(Node *head) {
  if (head == NULL) {
    cout << "NULL" << endl;
    return;
  }
  Node *temp = head;
  while (temp->next != NULL) {
    temp = temp->next;
  }
  while (temp != NULL) {
    cout << temp->data << "->";
    temp = temp->back;
  }
  cout << "NULL" << endl;
}

Node *reverse(Node *head) {
  Node *last = NULL;
  Node *temp = head;

  while (temp != NULL) {
    last = temp->back;
    temp->back = temp->next;
    temp->next = last;
    temp = temp->back;
  }

  return last->back;
}

int main() {
  vector<int> arr = {2, 5, 3, 9, 19};
  Node *head = convert2DLL(arr);
  insertBefore(head->next->next, 100);
  head = reverse(head);
  print(head);
  // printRev(head);

  return 0;
}

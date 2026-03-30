#include <bits/stdc++.h>
using namespace std;

// Node struct
struct Node {
public:
  Node *next;
  int value;

public:
  Node(int value1) {
    value = value1;
    next = NULL;
  }
  Node(int value1, Node *ptr) {
    value = value1;
    next = ptr;
  }
};

// Convert an array to linked list
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

// Traversing a linked list
void printLL(Node *head) {
  Node *temp = head;
  while (temp) {
    cout << temp->value << "->";
    temp = temp->next;
  }
  cout << "NULL" << endl;
}

int lengthOfLL(Node *head) {
  int cnt = 0;
  Node *temp = head;
  while (temp) {
    temp = temp->next;
    cnt++;
  }
  return cnt;
}

int checkIfPresent(Node *head, int target) {
  Node *temp = head;
  while (temp) {
    if (temp->value == target)
      return 1;
    temp = temp->next;
  }
  return 0;
}

Node *removeHead(Node *head) {
  Node *temp = head;
  head = head->next;
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
  Node *prev = NULL;
  Node *curr = head;
  // only one node exist
  while (curr->next != NULL) {
    prev = curr;
    curr = curr->next;
  }
  // head is tail
  prev->next = NULL;
  delete curr;
  return head;
}

Node *removeAt(Node *head, int pos) {
  if (head == NULL || pos < 0) {
    return head;
  }

  int cnt = 0;
  Node *prev = NULL;
  Node *curr = head;

  while (curr != NULL) {
    if (cnt == pos) {
      // Case1: removing head
      if (prev == NULL) {
        head = curr->next;
      } else {
        prev->next = curr->next;
      }
      delete curr;
      return head;
    }
    prev = curr;
    curr = curr->next;
    cnt++;
  }
  return head;
}

Node *removeValue(Node *head, int target) {
  if (head == NULL) {
    return head;
  }
  Node *prev = NULL;
  Node *curr = head;
  while (curr != NULL) {
    if (curr->value == target) {
      // Case1: removing head
      if (prev == NULL) {
        head = curr->next;
      } else {
        prev->next = curr->next;
      }
      delete curr;
      return head;
    }
    prev = curr;
    curr = curr->next;
  }
  return head;
}

Node *push_front(Node *head, int data) {
  Node *newNode = new Node(data);
  if (head == NULL) {
    head = newNode;
  } else {
    newNode->next = head;
    head = newNode;
  }
  return head;
}

Node *push_back(Node *head, int data) {
  Node *newNode = new Node(data);
  if (head == NULL) {
    head = newNode;
  } else {
    Node *temp = head;
    while (temp->next != NULL) {
      temp = temp->next;
    }
    temp->next = newNode;
  }
  return head;
}

Node *insert(Node *head, int data, int pos) {
  if (pos == 0) {
    return push_front(head, data);
  }

  Node *curr = head;
  int cnt = 0;

  while (curr != NULL && cnt < pos - 1) {
    curr = curr->next;
    cnt++;
  }

  if (curr == NULL) {
    return head;
  }

  Node *newNode = new Node(data);
  newNode->next = curr->next;
  curr->next = newNode;

  return head;
}

Node *insertBeforeValue(Node *head, int data, int val) {
  if (head == NULL) {
    return NULL;
  }
  if (head->value == val) {
    return new Node(data, head);
  }
  Node *temp = head;
  while (temp->next != NULL && temp->next->value != val) {
    temp = temp->next;
  }
  if (temp->next != NULL) {
    Node *newNode = new Node(data, temp->next);
    temp->next = newNode;
  }
  return head;
}

Node *reverse(Node *head) {
  Node *prev = NULL;
  Node *curr = head;
  Node *next = NULL;

  while (curr != NULL) {
    next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}

int main() {
  vector<int> arr = {1, 23, 35, 66, 88};
  Node *head = convertToLL(arr);
  int size = lengthOfLL(head);
  printLL(head);
  head = reverse(head);
  printLL(head);
  return 0;
}

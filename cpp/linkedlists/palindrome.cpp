#include <bits/stdc++.h>
using namespace std;

struct ListNode {
public:
  ListNode *next;
  int val;

public:
  ListNode(int value1) {
    val = value1;
    next = NULL;
  }
  ListNode(int value1, ListNode *ptr) {
    val = value1;
    next = ptr;
  }
};

bool ispalindrome(ListNode *head) {
  stack<int> st;

  ListNode *temp = head;
  // store elements is stack
  while (temp != NULL) {
    st.push(temp->val);
    temp = temp->next;
  }

  temp = head;
  // compare elements
  while (temp != NULL) {
    if (temp->val != st.top())
      return false;
    temp = temp->next;
    st.pop();
  }

  return true;
}

int main() { return 0; }

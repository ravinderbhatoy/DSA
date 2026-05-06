#include <iostream>
#include <stack>
#include <vector>
using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;

  Node(int value) {
    data = value;
    left = right = NULL;
  }
};

void preInPostOrder(Node *root, vector<int> &pre, vector<int> &in,
                    vector<int> &post) {

  stack<pair<Node *, int>> st;
  st.push({root, 1});
  if (root == NULL)
    return;

  while (!st.empty()) {
    auto it = st.top();
    st.pop();

    // this is part of pre
    // increment 1 to 2
    // push the left side of the tree
    if (it.second == 1) {
      pre.push_back(it.first->data);
      it.second++;
      st.push(it);

      if (it.first->left != NULL) {
        st.push({it.first->left, 1});
      }
    }

    // this is in part
    // increment 2 to 3
    // push right
    else if (it.second == 2) {
      in.push_back(it.first->data);
      it.second++;
      st.push(it);

      if (it.first->right != NULL) {
        st.push({it.first->right, 1});
      }
    }
    // don't push back again
    else {
      post.push_back(it.first->data);
    }
  }
}

int main() {

  Node *root = new Node(1);
  root->left = new Node(2);
  root->right = new Node(5);
  root->left->left = new Node(3);
  root->left->right = new Node(4);
  root->right->right = new Node(7);
  root->right->left = new Node(6);

  vector<int> pre;
  vector<int> in;
  vector<int> post;

  preInPostOrder(root, pre, in, post);

  cout << "Preorder traverse------" << endl;
  for (auto it : pre) {
    cout << it << " ";
  }
  cout << endl;

  cout << "Inorder traverse------" << endl;
  for (auto it : in) {
    cout << it << " ";
  }
  cout << endl;

  cout << "PostOrder traverse------" << endl;
  for (auto it : post) {
    cout << it << " ";
  }
  cout << endl;

  return 0;
}

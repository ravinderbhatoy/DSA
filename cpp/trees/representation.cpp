#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int data;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int value) {
    data = value;
    left = right = NULL;
  }
};

int main() {

  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->right = new TreeNode(5);

  return 0;
}

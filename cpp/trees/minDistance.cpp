#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int value) {
    val = value;
    left = right = NULL;
  }
};

class Solution {
public:
  int mini = INT_MAX;
  TreeNode *prev = NULL;
  int getMinimumDifference(TreeNode *root) {
    inOrder(root);
    return mini;
  }

private:
  void inOrder(TreeNode *node) {
    if (node == NULL)
      return;
    inOrder(node->left);

    if (prev != NULL) {
      mini = min(mini, node->val - prev->val);
    }
    prev = node;
    inOrder(node->right);
  }
};

int main() {

  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->right = new TreeNode(5);

  return 0;
}

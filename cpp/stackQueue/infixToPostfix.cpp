#include <bits/stdc++.h>
#include <cctype>
using namespace std;

int priority(char ch) {
  if (ch == '^') {
    return 3;
  } else if (ch == '*' || ch == '/') {
    return 2;
  } else if (ch == '+' || ch == '-') {
    return 1;
  }
  return -1;
}

string infixToPostfix(string exp) {
  stack<char> st;
  string postfix = "";

  for (int i = 0; i < exp.size(); i++) {
    char curr = exp[i];
    // check if it's an operand a -> z or A -> Z
    if (isalpha(curr)) {
      postfix += curr;
    }

    else if (curr == '(') {
      st.push('(');
    }

    // add all to postfix if closing parenthesis occured
    else if (curr == ')') {
      while (!st.empty() && st.top() != '(') {
        postfix += st.top();
        st.pop();
      }
      st.pop();
    }

    else {
      // shift all high priority from stack to postfix
      while (!st.empty() && priority(st.top()) >= priority(curr)) {
        postfix += st.top();
        st.pop();
      }
      st.push(curr);
    }
  }
  // empty stack
  while (!st.empty()) {
    postfix += st.top();
    st.pop();
  }
  return postfix;
}

int main() {
  string infix = "a+b*(c^d-e)";
  string postfix = infixToPostfix(infix);
  cout << postfix << endl;
  return 0;
}

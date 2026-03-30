#include <bits/stdc++.h>
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

string infixToPrefix(string exp) {
  // 1. reverse
  reverse(exp.begin(), exp.end());
  // 2. convert '(' -> ')' and ')' -> '('
  for (int i = 0; i < exp.size(); i++) {
    if (exp[i] == ')') {
      exp[i] = '(';
    } else if (exp[i] == '(') {
      exp[i] = ')';
    }
  }
  stack<char> st;
  string prefix = "";
  // 3. infix to postfix
  for (char curr : exp) {
    // check if it's an operand a -> z or A -> Z
    if (isalpha(curr)) {
      prefix += curr;
    }

    else if (curr == '(') {
      st.push('(');
    }

    else if (curr == ')') {
      // add all to postfix if closing parenthesis occured
      while (!st.empty() && st.top() != '(') {
        prefix += st.top();
        st.pop();
      }
      st.pop();
    }

    else {

      if (curr == '^') {
        while (!st.empty() && priority(curr) <= priority(st.top())) {
          prefix += st.top();
          st.pop();
        }
      }

      else {
        while (!st.empty() && priority(curr) < priority(st.top())) {
          prefix += st.top();
          st.pop();
        }
      }

      st.push(curr);
    }
  }

  // empty stack
  while (!st.empty()) {
    prefix += st.top();
    st.pop();
  }

  // 4. reverse
  reverse(prefix.begin(), prefix.end());
  return prefix;
}

int main() {
  string infix = "a+b*(c^d-e)";
  infix = "(a+b)*c-d+f";
  string prefix = infixToPrefix(infix);
  cout << prefix << endl;
  return 0;
}

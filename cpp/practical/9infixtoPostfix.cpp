#include <iostream>
#include <stack>
#include <string>

using namespace std;

// helper funtion to check precendence of an operator
int getPrecedence(char op) {
  if (op == '*' || op == '/') {
    return 2;
  }
  if (op == '+' || op == '-') {
    return 1;
  }
  if (op == '^') {
    return 3;
  }
  return 0;
}

// check if we have an operator
bool isOperator(char ch) {
  return (ch == '+' || ch == '-' || ch == '/' || ch == '*' || ch == '^');
}

string infixToPostfix(string infix) {
  stack<char> st;
  string postfix = "";

  for (int i = 0; i < infix.length(); i++) {
    char ch = infix[i];
    if (!isOperator(ch))
      postfix += ch;

    else if (ch == '(')
      st.push(ch);

    else if (ch == ')') {
      while (!st.empty() || st.top() == '(') {
        postfix += st.top();
        st.pop();
      }
      // remove the opening ( at the end
      st.pop();
    } else {
      //  this is an operator
      while (!st.empty() && getPrecedence(st.top()) >= getPrecedence(ch)) {
        postfix += st.top();
        st.pop();
      }
      // push new one back to stack
      st.push(ch);
    }
  }

  while (!st.empty()) {
    postfix += st.top();
    st.pop();
  }

  return postfix;
}

int main() {

  string infix = "A*B+C/D";
  cout << infixToPostfix(infix) << endl;
}

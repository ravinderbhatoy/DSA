#include <bits/stdc++.h>
using namespace std;

bool validParenthesis(string s) {
  stack<char> st;
  for (int i = 0; i < s.size(); i++) {

    if (s[i] == '[' || s[i] == '(' || s[i] == '{' || st.empty()) {
      st.push(s[i]);
    } else if (s[i] == ']' && st.top() == '[') {
      st.pop();
    } else if (s[i] == ')' && st.top() == '(') {
      st.pop();
    } else if (s[i] == '}' && st.top() == '{') {
      st.pop();
    } else {
      return false;
    }
  }
  return st.empty();
}

int main() { return 0; }

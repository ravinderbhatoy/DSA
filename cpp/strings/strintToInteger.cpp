#include <bits/stdc++.h>
#include <climits>
using namespace std;

int atoi(string s) {
  int i = 0;
  int sign = 1;
  long long num = 0;

  // remove white space
  while (i < s.size() && s[i] == ' ')
    i++;

  // check for sign
  if (s[i] == '-' || s[i] == '+') {
    sign = s[i] == '-' ? -1 : 1;
    i++;
  }

  while (i < s.size() && isdigit(s[i])) {
    num = num * 10 + (s[i] - '0');
    if (num >= INT_MAX)
      return INT_MAX;
    if (num <= INT_MIN)
      return INT_MIN;
    i++;
  }

  return (int)(sign * num);
}

int main() {

  string s = "  -042";
  cout << atoi(s);

  return 0;
}

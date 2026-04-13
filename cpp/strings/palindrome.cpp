#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(string s) {

  int st = 0, size = s.length(), end = size - 1;
  if (size == 1)
    return true;
  while (st < end) {
    if (!isalnum(s[st])) {
      st++;
      continue;
    }
    if (!isalnum(s[end])) {
      end--;
      continue;
    }

    if (tolower(s[st]) != tolower(s[end])) {
      return false;
    }
    st++;
    end--;
  }
  return true;
}

int main() {

  string s = "A man, a plan, a canal : Panama ";

  cout << s.find("man") << endl;
  s.erase(s.find("man"), 3);
  cout << s << endl;

  cout << isPalindrome(s);

  return 0;
}

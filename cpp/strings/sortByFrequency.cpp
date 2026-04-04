#include <bits/stdc++.h>
#include <iterator>
using namespace std;

string sortByFrequency(string s) {
  int count = 1;
  string ans;

  int preMax = 1;

  for (int i = 0; i < s.size() - 1; i++) {
    char curr = s[i];
    count = 1;
    while (curr == s[i + 1]) {
      count++;
      i++;
    }
    cout << "adding  " << s[i] << endl;
    if (i > 0 && count >= preMax) {
      cout << i - count << count << endl;
      ans = s.substr(i - count, count + 1) + ans;
      preMax = count;
    } else if (i > 0 && count < preMax) {
      ans += s.substr(i - count, count + 1);
    } else {
      cout << "adding  " << s[i] << endl;
      ans += s[i];
    }
  }
  return ans;
}

int main() {

  string s = "abbdccc";
  cout << sortByFrequency(s) << endl;

  return 0;
}

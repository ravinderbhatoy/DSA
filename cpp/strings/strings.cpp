#include <iostream>
using namespace std;

int main() {

  // char str[100];
  // cout << "Enter string: ";
  // // cin >> str; // space not supported
  // cin.getline(str, 100);
  // cout << "Output: " << str << endl;

  // string are dynamic in nature characters array are not
  string str;
  getline(cin, str);

  cout << str;

  return 0;
}

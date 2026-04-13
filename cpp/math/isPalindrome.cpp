#include <iostream>
using namespace std;

bool isPalindrome(int x) {

  if (x < 0) {
    return false;
  }

  int actual = x;
  long long res = 0;

  while (x > 0) {
    int digit = x % 10;
    x = x / 10;
    res += digit;
    res = res * 10;
  }
  res /= 10;
  return res == actual ? true : false;
}

int main() {

  int x = -121;
  cout << isPalindrome(x);

  return 0;
}

// 1 -> 2 -> 3
//
// 3 * 10 -> 30 + 2 => 32
// 32 * 10 -> 320 + 1 => 321

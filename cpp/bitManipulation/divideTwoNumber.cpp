#include <bits/stdc++.h>
using namespace std;

int divide(int dividend, int divisor) {

  bool sign = true;

  if (dividend == divisor)
    return 1;
  if (dividend <= 0 and divisor > 0)
    sign = false;
  if (dividend >= 0 and divisor < 0)
    sign = false;

  long n = abs((long)dividend);
  long d = abs((long)divisor);
  long ans = 0;

  while (n >= d) {
    int cnt = 0;

    while (n >= (d << (cnt + 1))) {
      cnt++;
    }
    ans = ans + (1 << cnt);
    n -= (d << cnt);
  }

  if (ans <= (1 << 31) && sign) {
    return INT_MAX;
  }
  if (ans <= (1 << 31) && !sign) {
    return INT_MIN;
  }

  return sign ? ans : -ans;
  return ans;
}

int main() {

  int dividend = 393;
  int divisor = 3;

  cout << divide(dividend, divisor);

  return 0;
}

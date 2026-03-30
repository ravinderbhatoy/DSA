#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

bool isValid(vector<int> &blocks, int m, int maxAllowedUnits) {
  int painters = 1;
  int units = 0;

  for (int i = 0; i < blocks.size(); i++) {
    if (blocks[i] > maxAllowedUnits)
      return false;
    if (units + blocks[i] <= maxAllowedUnits) {
      units += blocks[i];
    } else {
      painters++;
      units = blocks[i];
    }
  }

  return painters <= m;
}

int allocateUnitsTime(vector<int> &blocks, int m) {
  int sum = 0, maxVal = -1;

  for (auto units : blocks) {
    sum += units;
    maxVal = max(units, maxVal);
  }

  int st = maxVal, end = sum, ans = -1;

  while (st <= end) {
    int mid = st + (end - st) / 2;

    if (isValid(blocks, m, mid)) {
      end = mid - 1;
      ans = mid;
    } else {
      st = mid + 1;
    }
  }

  return ans;
}

int main() {

  vector<int> blocks = {40, 30, 10, 20};

  cout << allocateUnitsTime(blocks, 2);

  return 0;
}

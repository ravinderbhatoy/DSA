#include <iostream>
#include <vector>
using namespace std;

vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid) {
  int n = grid.size();
  vector<int> ans(2, 0);
  vector<int> hash(n * n + 1, 0);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      hash[grid[i][j]]++;
    }
  }

  for (int i = 0; i < hash.size(); i++) {
    if (hash[i] == 0)
      ans[1] = i;
    else if (hash[i] == 2)
      ans[0] = i;
  }

  return ans;
}

int main() {

  vector<vector<int>> grid = {{1, 3}, {2, 2}};

  vector<int> ans = findMissingAndRepeatedValues(grid);

  for (int ele : ans) {
    cout << ele << " ";
  }
}

#include <bits/stdc++.h>
using namespace std;

int main() {

  // matrix representation
  // int n, m;
  // cin >> n >> m;
  // int mat[n + 1][n + 1];
  //
  // for (int i = 0; i < m; i++) {
  //   int u, v;
  //   cin >> u >> v;
  //   mat[u][v] = 1;
  //   mat[v][u] = 1;
  // }

  cout << "Running...\n";
  int n, m;
  cin >> n >> m;
  vector<vector<int>> adj(n + 1);

  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }

  for (int i = 1; i <= n; i++) {
    cout << i << " -> ";
    for (int node : adj[i]) {
      cout << node << " ";
    }
    cout << endl;
  }

  return 0;
}

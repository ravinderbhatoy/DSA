#include <bits/stdc++.h>
using namespace std;

int main() {

  int n, m;
  cout << "Enter no. of edges: ";
  cin >> m;
  cout << "Enter no. of nodes: ";
  cin >> n;

  vector<vector<int>> nodes;
  vector<vector<int>> adj(n, vector<int>(n, 0));

  while (m--) {
    int u, v;
    cin >> u >> v;
    if (u < n && v < n) { // Boundary check
      adj[u][v] = 1;      // incase of weighted graph store weight != 1 = weight
      adj[v][u] = 1;
    }
  }

  cout << "Printing Adjaney matrix: " << endl;

  for (auto ele : adj) {
    for (auto v : ele) {
      cout << v << " ";
    }
    cout << endl;
  }

  return 0;
}

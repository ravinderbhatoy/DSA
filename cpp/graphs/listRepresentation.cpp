#include <iostream>
#include <vector>
using namespace std;

int main() {

  int n, m;
  cin >> m >> n;

  vector<int> adj[n + 1];

  while (m--) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u); // not needed for directed graph (u -> v)
  }
  // incase of weighted graph store pairs with weights
  // (node, weight), (node1, weight)..

  return 0;
}

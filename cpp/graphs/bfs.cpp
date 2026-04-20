#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> bfs(int start, int n, vector<int> adj[]) {
  vector<int> res;
  vector<int> vis(n + 1, 0);
  queue<int> q;
  vis[start] = 1;
  q.push(start);

  while (!q.empty()) {
    int node = q.front();
    q.pop();
    res.push_back(node);

    for (auto it : adj[node]) {
      if (!vis[it]) {
        vis[it] = 1;
        q.push(it);
      }
    }
  }

  return res;
}

int main() {

  int n, m;
  cout << "Enter no. of vertices: ";
  cin >> n;
  cout << "Enter no. of edges: ";
  cin >> m;

  vector<int> adj[n + 1];

  while (m--) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u); // not needed for directed graph (u -> v)
  }
  // incase of weighted graph store pairs with weights
  // (node, weight), (node1, weight)..
  //
  int start = 1;
  vector<int> res = bfs(start, n, adj);
  for (auto ele : res) {
    cout << ele << " ";
  }
  cout << endl;

  return 0;
}

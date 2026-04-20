#include <iostream>
#include <vector>
using namespace std;

void dfs(int start, vector<int> &visited, vector<int> adj[], vector<int> &ans) {
  visited[start] = 1;
  ans.push_back(start);
  for (auto n : adj[start]) {
    if (!visited[n]) {
      dfs(n, visited, adj, ans);
    }
  }
}

vector<int> dfsGraph(int start, int n, vector<int> adj[]) {
  vector<int> visited(n + 1, 0);
  vector<int> ans;

  dfs(start, visited, adj, ans);
  return ans;
}

int main() {

  int n, m;
  cout << "Enter no. of vertices: ";
  cin >> n;
  cout << "Enter no. of edges: ";
  cin >> m;

  vector<int> adj[n + 1]; // assuming the starting node as 1

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
  vector<int> res = dfsGraph(start, n, adj);
  for (auto ele : res) {
    cout << ele << " ";
  }
  cout << endl;

  return 0;
}

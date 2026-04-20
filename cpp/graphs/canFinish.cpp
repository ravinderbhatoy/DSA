#include <bits/stdc++.h>
#include <queue>
using namespace std;

vector<vector<int>> convertToAdjList(const vector<vector<int>> &matrix) {
  int n = matrix.size();
  vector<vector<int>> adj(n);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      // Only add once. If it's an undirected graph,
      // matrix[i][j] and matrix[j][i] are both 1.
      // We only process one side of the diagonal or simply add j to adj[i].
      if (matrix[i][j] == 1 && i != j) {
        adj[i].push_back(j);
      }
    }
  }
  return adj;
}

bool isDetected(int src, vector<vector<int>> adj, vector<int> &vis) {
  vis[src] = 1;
  queue<pair<int, int>> que;
  que.push({src, -1});

  while (!que.empty()) {
    int node = que.front().first;
    int parent = que.front().second;
    que.pop();

    for (auto adjNode : adj[node]) {
      if (!vis[adjNode]) {
        vis[adjNode] = 1;
        que.push({adjNode, node});
      } else if (parent != adjNode) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  int numCourses = 2;
  vector<int> vis(numCourses, 0);
  vector<vector<int>> prerequisites = {{1, 0}};

  vector<vector<int>> adjList = convertToAdjList(prerequisites);

  cout << isDetected(0, adjList, vis);

  return 0;
}

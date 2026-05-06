#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {

  // create adjacency list
  vector<pair<int, int>> adj[V];
  for (auto &edge : edges) {
    int u = edge[0];
    int v = edge[1];
    int w = edge[2];

    adj[u].push_back({v, w});
    adj[v].push_back({u, w}); // graph is undirected
  }

  // initialize min heap
  priority_queue<pair<int, int>, vector<pair<int, int>>,
                 greater<pair<int, int>>>
      pq;

  vector<int> dist(V, 1e9);

  // source node distance
  dist[src] = 0;
  pq.push({0, src}); // (distance, node)

  while (!pq.empty()) {
    int dis = pq.top().first;
    int node = pq.top().second;
    pq.pop();

    for (auto it : adj[node]) {
      int adjNode = it.first;
      int edgeWeight = it.second;

      if (dis + edgeWeight < dist[adjNode]) {
        dist[adjNode] = dis + edgeWeight;
        pq.push({dist[adjNode], adjNode});
      }
    }
  }

  return dist;
}

int main() {

  int V = 3;
  vector<vector<int>> edges = {{0, 1, 1}, {1, 2, 3}, {0, 2, 6}};
  int src = 2;

  vector<int> res = dijkstra(V, edges, src);
  for (auto it : res)
    cout << it << " ";
  cout << endl;

  return 0;
}

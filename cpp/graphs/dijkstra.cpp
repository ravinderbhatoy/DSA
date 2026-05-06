#include <bits/stdc++.h>
using namespace std;

vector<int> dijkstra(int V, vector<vector<int>> adj[], int S) {
  set<pair<int, int>> st;
  vector<int> dist(V, 1e9);

  st.insert({0, S});
  dist[S] = 0;

  while (!st.empty()) {
    auto it = *(st.begin());
    int node = it.second;
    int dis = it.first;
    st.erase(it);

    for (auto it : adj[node]) {
      int adjNode = it[0]; // Adjacent node
      int edgW = it[1];    // Weight of the edge
      if (dis + edgW < dist[adjNode]) {
        if (dist[adjNode] != 1e9)
          st.erase({dist[adjNode], adjNode});

        dist[adjNode] = dis + edgW;
        st.insert({dist[adjNode], adjNode});
      }
    }
  }
  return dist;
}
int main() {
  int V, E, S;
  cout << "Enter number of Vertices (V), Edges (E), and Source Node (S):"
       << endl;
  if (!(cin >> V >> E >> S))
    return 0;

  vector<vector<int>> adj[V];

  cout << "Enter " << E << " edges in format: u v weight" << endl;
  for (int i = 0; i < E; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back({v, w});
  }

  vector<int> res = dijkstra(V, adj, S);

  cout << "\n--- Shortest Path Results ---" << endl;
  for (int i = 0; i < V; i++) {
    cout << "Path " << S << " -> " << i << " : ";
    if (res[i] == 1e9)
      cout << "Unreachable" << endl;
    else
      cout << res[i] << " units" << endl;
  }

  return 0;
}

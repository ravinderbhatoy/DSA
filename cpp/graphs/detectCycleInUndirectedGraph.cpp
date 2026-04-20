#include <queue>
#include <vector>
using namespace std;

bool detectCycle(int n, vector<int> adj[]) {
  vector<int> visited(n, 0);
  queue<pair<int, int>> q;
  // 0 as source node
  visited[0] = 1;
  q.push({0, -1});

  while (!q.empty()) {
    int node = q.front().first;
    int parent = q.front().second;
    q.pop();

    for (auto adjNode : adj[node]) {
      if (!visited[adjNode]) {
        visited[adjNode] = 1;
        q.push({adjNode, node});
      }

      else if (parent != adjNode) {
        return true;
      }
    }
  }

  return false;
}

int main() { return 0; }

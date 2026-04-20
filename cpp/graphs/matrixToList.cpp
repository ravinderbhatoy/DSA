#include <iostream>
#include <vector>
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

int main() {
  int n = 3; // Using 3 for a quick example
  vector<vector<int>> matrix(n, vector<int>(n));

  cout << "Enter " << n << "x" << n << " adjacency matrix:" << endl;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> matrix[i][j];
    }
  }

  vector<vector<int>> adj = convertToAdjList(matrix);

  cout << "\nAdjacency List representation:" << endl;
  for (int i = 0; i < adj.size(); i++) {
    cout << "Node " << i << ": ";
    for (int neighbor : adj[i]) {
      cout << neighbor << " ";
    }
    cout << endl;
  }

  return 0;
}

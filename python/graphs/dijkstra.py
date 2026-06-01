import heapq


class Solution:

    # Function to find the shortest distance of all the vertices from
    # the source vertex S
    def dijkstra(self, V, adj, S):
        # Create a priority queue to store the nodes as a pair {dist, node}
        # The queue will always return the node with
        # the smallest distance first
        pq = []

        # Initialising dist list with a large number to indicate the nodes are
        # unvisited initially
        dist = [float('inf')] * V
        dist[S] = 0

        # Push the source node with distance 0 into the priority queue
        heapq.heappush(pq, (0, S))

        while pq:
            # Pop the node with the smallest distance
            dis, node = heapq.heappop(pq)

            # Traverse all the adjacent nodes
            for adjNode, weight in adj[node]:
                # If the new calculated distance is smaller, update it
                if dis + weight < dist[adjNode]:
                    dist[adjNode] = dis + weight
                    heapq.heappush(pq, (dist[adjNode], adjNode))

        return dist


# Driver code
if __name__ == "__main__":
    # Number of vertices and edges
    V = 3
    E = 3
    S = 2

    # Create adjacency list to represent the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    adj[0].append((1, 1))
    adj[0].append((2, 6))
    adj[1].append((2, 3))
    adj[1].append((0, 1))
    adj[2].append((1, 3))
    adj[2].append((0, 6))

    # Create an instance of the Solution class
    obj = Solution()
    # Call dijkstra function and store the result
    res = obj.dijkstra(V, adj, S)

    # Output the shortest distance from source to all nodes
    print(" ".join(map(str, res)))

from collections import defaultdict
import heapq

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        adj = defaultdict(list)
        m = len(maze)
        n = len(maze[0])

        for i in range(m):
            for j in range(n):
                if maze[i][j] == '+':
                    continue
                # Left
                if j != 0 and maze[i][j-1] != "+":
                    adj[(i, j)].append((i, j-1))
                # Right
                if j != n-1 and maze[i][j+1] != "+":
                    adj[(i, j)].append((i, j+1))
                # Up
                if i != 0 and maze[i-1][j] != "+":
                    adj[(i, j)].append((i-1, j))
                # Down
                if i != m-1 and maze[i+1][j] != "+":
                    adj[(i, j)].append((i+1, j))
        
        # print(f"Adjacency List: {adj}")

        def dijkstra(adj, entrance, m, n):
            min_dist = float('inf')
            distances = {node: float('inf') for node in adj}
            distances[entrance] = 0

            priority_queue = [(0, entrance)]

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
            
                if (current_node[0] in [0, m-1] or current_node[1] in [0, n-1]) and current_node != entrance:
                    # print(f'Current Node: {current_node}')
                    # print(f'Entrance Node: {entrance}')
                    min_dist = min(min_dist, current_distance)

                if current_distance > distances[current_node]:
                    continue
                
                for nb_node in adj[current_node]:
                    distance = current_distance + 1
                    if distance < distances[nb_node]:
                        distances[nb_node] = distance
                        heapq.heappush(priority_queue, (distance, nb_node))

            # print(f'Distances: {distances}')

            return min_dist if min_dist != float('inf') else -1

        return dijkstra(adj, tuple(entrance), m, n)

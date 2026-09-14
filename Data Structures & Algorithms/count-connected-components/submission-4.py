from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n_components = 0
        visited_nodes = [0 for _ in range(n)]
        neighbors = {i:set() for i in range(n)}

        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
        
        def bfs(node):
            queue = deque()
            queue.append(node)
            visited_nodes[node] = 1
            while queue:
                current = queue.popleft()
                neighbor_set = neighbors[current]
                for neighbor in neighbor_set:
                    if visited_nodes[neighbor]==0:
                        queue.append(neighbor)
                        visited_nodes[neighbor] = 1
        
        for node in range(n):
            if visited_nodes[node] == 0:
                bfs(node)
                n_components += 1
        
        return n_components
                    

        
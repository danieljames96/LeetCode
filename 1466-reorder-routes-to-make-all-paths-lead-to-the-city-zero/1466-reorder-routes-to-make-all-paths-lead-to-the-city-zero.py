from collections import defaultdict

class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = set()
        g = defaultdict(list)

        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
            s.add((a, b))

        vis = [False] * n

        def dfs(u):
            vis[u] = True
            ans = 0 
            
            for v in g[u]:
                if not vis[v]:
                    if (u, v) in s:
                        ans += 1
                    ans += dfs(v)
            return ans

        return dfs(0)
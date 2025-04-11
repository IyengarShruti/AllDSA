class Solution:
    """
    Approach:
    - ek adjacency matrix diya gaya hai (isConnected), jisme cities ka connection dikh raha hai.
    - Har connected group of cities ko ek 'province' kehte hai.
    - Hum DFS se har unvisited node se saari connected cities visit karenge.
    - Har baar jab naye node se DFS start karte hai => ek naya group mila (count++) \U0001f3d9️

    Time Complexity: O(n^2) -> Har cell check karna padta hai matrix mein
    Space Complexity: O(n) -> visited[] array use kiya hai
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)             # Total number of cities/nodes
        visited = [False] * n            # Kisi city ko visit kiya ya nahi
        count = 0                        # Kitne groups/provinces mile

        for i in range(n):
            if not visited[i]:
                count += 1               # Naya group mila bhai \U0001f389
                self.dfs(isConnected, i, visited)  # Ab uss group ke sabko visit karo
        
        return count

    def dfs(self, adj: List[List[int]], u: int, visited: List[bool]):
        visited[u] = True               # Is node ko visit mark kar diya ✅

        for v in range(len(adj)):
            # Agar connection hai aur wo city abhi tak visit nahi hui
            if adj[u][v] == 1 and not visited[v]:
                # Chalo chalo uss neighbour pe bhi DFS maarte hai \U0001f6b6‍♂️
                self.dfs(adj, v, visited)

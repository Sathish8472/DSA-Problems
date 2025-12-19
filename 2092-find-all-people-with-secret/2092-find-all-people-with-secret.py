class Solution:
    def dfs(self, x, adj, vis):
        vis[x] = True
        for nei in adj.get(x, []):
            if not vis[nei]:
                self.dfs(nei, adj, vis)

    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        ans = []
        vis = [False] * n
        vis[0] = True
        vis[firstPerson] = True

        meetings.sort(key=lambda a: a[2])
        i = 0

        while i < len(meetings):
            time = meetings[i][2]
            adj = {}
            secret = set()

            while i < len(meetings) and meetings[i][2] == time:
                x, y = meetings[i][0], meetings[i][1]

                if x not in adj:
                    adj[x] = []
                if y not in adj:
                    adj[y] = []

                adj[x].append(y)
                adj[y].append(x)

                if vis[x]:
                    secret.add(x)
                if vis[y]:
                    secret.add(y)

                i += 1

            for s in secret:
                self.dfs(s, adj, vis)

        for j in range(n):
            if vis[j]:
                ans.append(j)

        return ans
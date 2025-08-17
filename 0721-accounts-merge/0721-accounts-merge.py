class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)

        mapMailNode = {}

        for i in range(n):
            for mail in accounts[i][1:]:
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                
                else:
                    ds.unionBySize(i, mapMailNode[mail])
        
        mergedMail = [[] for _ in range(n)]
        for mail, node in mapMailNode.items():
            root = ds.findUPar(node)
            mergedMail[root].append(mail)

        ans = []
        for i in range(n):
            if not mergedMail[i]:
                continue
            
            mergedMail[i].sort()
            temp = [accounts[i][0]] + mergedMail[i]
            ans.append(temp)

        ans.sort()
        return ans
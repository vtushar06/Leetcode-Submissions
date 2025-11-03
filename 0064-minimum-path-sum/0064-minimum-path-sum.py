class Solution:
    def minPathSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        adj=[[] for i in range(n*m)]
        directions=[[0,1],[1,0]]
        for i in range(n):
            for j in range(m):
                node=m*i+j
                for di,dj in directions:
                    ni,nj=i+di,j+dj
                    if(0<=ni<n and 0<=nj<m):
                        newnode=m*ni+nj
                        adj[node].append([newnode,mat[ni][nj]])

        import heapq
        dis=[float("inf")]*(n*m)
        dis[0]=mat[0][0]
        pq=[(mat[0][0],0)]

        while pq:
            distance,node=heapq.heappop(pq)

            if distance > dis[node]:
                continue

            for neigh,weight in adj[node]:
                newdis=distance+weight
                if newdis< dis[neigh]:
                    dis[neigh]=newdis
                    heapq.heappush(pq,(newdis,neigh))

        return dis[n*m-1]
        
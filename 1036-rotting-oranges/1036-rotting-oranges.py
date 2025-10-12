from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshoranges=0
        minutes=0
        n,m=len(grid),len(grid[0])
        queue=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                elif grid[i][j]==1:
                    freshoranges+=1
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            x,y,time=queue.popleft()
            minutes=max(minutes,time)
            for dx,dy in directions:
                nx=x+dx
                ny=y+dy
                if(0<=nx and nx<n and 0<=ny and ny<m and grid[nx][ny]==1):
                    queue.append((nx,ny,time+1))
                    grid[nx][ny]=2
                    freshoranges-=1
        return minutes if freshoranges==0 else -1            



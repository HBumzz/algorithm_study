import sys
from collections import deque
sys.stdin =open('input.txt', 'r')
def bfs(n):
    global v
    q = deque()
    v = [100001 for _ in range(N+1)]
    q.append(n)
    while q:
        t = q.popleft()
        for i in adj[t]:
            if adj[i[0]][1]<v[i[0]]:
                pass
N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int,input().split())
    adj[a].append([b,c])
print(adj)
A, B = map(int,input().split())
bfs(A)
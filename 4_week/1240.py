import sys
from collections import deque
sys.stdin = open('input.txt','r')

def bfs(start, end):
    global ans
    q = deque()
    q.append([start,0])
    v = [0] * (N + 1)
    v[start] = 1
    while q:
        t, d = q.popleft()
        if t == end:
            ans = d
            break
        for s in adj[t]:
            if v[s] == 0:
                v[s] = 1
                q.append([s, d+distance[t][s]])

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)] # 0부터 N까지의 인접행렬
distance = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1):
    a, b, dist = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    distance[a][b] = dist
    distance[b][a] = dist

for i in range(M):
    start, end = map(int, input().split())
    bfs(start, end)
    print(ans)
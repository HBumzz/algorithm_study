from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def bfs(n):
    v[n] = 1
    q = deque()
    q.append(n)
    while q:
        t = q.popleft()
        for k in adj[t]:
            if v[k] == 0 :
                v[k] = 1
                q.append(k)
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int , input().split())
    adj[a].append(b)
    adj[b].append(a)
v = [0] * (N + 1)
cnt = 0
for i in range(1, N+1):
    if not v[i]:
        bfs(i)
        cnt += 1
print(cnt)
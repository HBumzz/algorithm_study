import sys
import heapq
input = sys.stdin.readline
def bfs(start):
    q = []
    heapq.heappush(q, (0,start))
    visited[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        for i in adj[now]:
            cost = dist+i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
V, E = map(int, input().split())
INF = 10*(E+1)
start = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,e = map(int, input().split())
    adj[u].append((v,e))
visited = [INF] * (V + 1)
bfs(start)
for i in range(1,V+1):
    if visited[i] == INF:
        print('INF')
    else:
        print(visited[i])
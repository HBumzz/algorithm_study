import sys
import heapq

def dijkstra(start):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue

        for adj_node, adj_cost in adj[node]:
            new_cost = distance[node] + adj_cost
            if new_cost < distance[adj_node]:
                distance[adj_node] = new_cost
                heapq.heappush(q, (new_cost, adj_node))

    return distance

N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> N
d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

ans1 = d1[v1] + d2[v2] + d3[N]
ans2 = d1[v2] + d3[v1] + d2[N]
ans = min(ans1, ans2)

if ans >= float('inf'):
    ans = -1

print(ans)
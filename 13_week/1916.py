import sys
input = sys.stdin.readline
import heapq
def dajkstra(start,end):
    v = [10e8]*(N+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        distance, node = heapq.heappop(q)
        if distance > v[node]:
            continue
        for n_node, n_distance in adj[node]:
            if n_distance + distance < v[n_node] :
                v[n_node] = n_distance + distance
                heapq.heappush(q, (distance+n_distance, n_node))
    return v[end]
N = int(input())
k = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(k):
    a,b, dist = map(int, input().split())
    adj[a].append((b,dist))
start, end = map(int,input().split())

ans = dajkstra(start,end)
print(ans)
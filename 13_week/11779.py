import heapq
import sys
input = sys.stdin.readline
def dajkstra(start,end):
    q = []
    v = [10e9 for _ in range(city_N+1)]
    path = [[] for _ in range(city_N+1)]
    heapq.heappush(q,(0,start,[start]))
    v[start] = 0
    while q:
        time, position, p = heapq.heappop(q)
        if time > v[position]:
            continue
        for n_postion, n_time in adj[position]:
            if time+n_time < v[n_postion] :
                v[n_postion] = time + n_time
                path[n_postion] = p + [n_postion]
                heapq.heappush(q, (time+n_time, n_postion, p+ [n_postion]))
    return v[end] ,path[end]
city_N = int(input())
N = int(input())
adj = [[] for _ in range(city_N+1)]
for _ in range(N):
    a, b, cost = map(int, input().split())
    adj[a].append((b, cost))
start, end = map(int, input().split())
ans1, ans3 = dajkstra(start,end)
ans2 = len(ans3)
print(ans1)
print(ans2)
print(*ans3)
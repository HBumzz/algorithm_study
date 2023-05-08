import heapq
N,M = map(int,input().split())
q = list(map(int, input().split()))
q.sort()
for i in range(M):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)
print(sum(q))
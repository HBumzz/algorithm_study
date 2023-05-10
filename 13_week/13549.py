from collections import deque
N, K = map(int, input().split())

def bfs(N):
    v = [0]*(100001)
    q = deque()
    q.append([N,0])
    while q:
        pos, time = q.popleft()
        if pos == K:
            return time
        if v[pos]:
            continue
        v[pos] = 1
        if pos*2 <= 100000:
            q.append([pos*2, time])
        if pos-1 >=0:
            q.append([pos-1,time+1])
        if pos+1 <= 100000:
            q.append([pos+1,time+1])
a = bfs(N)
print(a)
from collections import deque
N, K = map(int, input().split())


def bfs(N):
    global v
    v = [0]*(100001)
    q = deque()
    q.append([N,0])
    min_time = 100001
    cnt = 0
    while q:
        pos, time = q.popleft()
        if pos == K:
            if min_time == 100001:
                min_time = time
            if time == min_time:
                cnt += 1
        for i in (pos-1, pos+1, pos*2):
            if 0<=i <= 100000 and (v[i] == 0 or v[i] == time + 1):
                v[i] = time + 1
                q.append([i,time+1])
    return min_time, cnt
a,b = bfs(N)
print(a)
print(b)
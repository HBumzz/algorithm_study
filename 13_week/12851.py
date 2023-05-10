from collections import deque
N, K = map(int, input().split())


def bfs(N):
    global v
    v = [0]*(100001)
    q = deque()
    flag = 0
    q.append([N,0,flag])
    while q:
        pos, time, f = q.popleft()
        if pos == K:
            global t
            t = time
            f +=1
            if time > t :
                return f
        for i in ((pos-1, pos+1, pos*2)):
            if 0<=i <= 100000 and v[i] == 0:
                q.append([i,time+1,f])
                v[i] = 1 # 첫번째 정답

ans2 = bfs(N)
print(t)
print(ans2)
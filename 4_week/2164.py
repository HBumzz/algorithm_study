from collections import deque
N =int(input())
q = deque()
for i in range(1,N+1):
    q.append(i)
while q:
    if len(q) == 1:
        break
    q.popleft()
    q.append(q.popleft())
print(q[0])
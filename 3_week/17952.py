import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
minute = int(input())
stk = []
ans = 0
for _ in range(minute):
    lst = list(map(int, input().split()))
    if len(lst) == 3:
        stk.append([lst[1],lst[2]])
    if stk:
        a = stk.pop()
        t = a[1] -1
        if t == 0:
            ans+= a[0]
        else:
            stk.append([a[0],t])
print(ans)
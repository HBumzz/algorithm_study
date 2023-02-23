import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
stk = []
ans = [0]*N
past_lst = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.append([i,past_lst[i]])
for i in range(N):
    if not stk :
        stk.append(lst[i])
    elif stk and stk[-1][1] >= lst[i][1]:
        stk.append(lst[i])
    elif stk and stk[-1][1] < lst[i][1]:
        while True:
            if stk and stk[-1][1] >= lst[i][1]:
                break
            if stk:
                a = stk.pop()
                ans[a[0]] = lst[i][1]
            else:
                break
        stk.append(lst[i])
if stk :
    while stk:
        p = stk.pop()
        ans[p[0]] = -1
print(*ans)
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
stk = []
ans = []
lst = list(map(int, input().split()))
for i in lst:
    if not stk:
        stk.append(i)
    else:
        if stk[-1] <i:
            stk.append(i)
        else:
            while True: # stk에는 오큰수를 못찾은 수들이 담겨잇음
                stk.pop()
                stk.append(i)
                ans.append(i)
                if stk[-1] >= i:
                    break
    print(stk)
print(ans)
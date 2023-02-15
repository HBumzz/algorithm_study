import sys
sys.stdin = open('input.txt', 'r')

def check(left, right, cnt):
    while left <= right :
        if Str[left] != Str[right] and cnt ==0:
            a = check(left+1, right, cnt+1)
            b = check(left, right-1, cnt+1)
            cnt = min(a,b)
            return cnt
        elif Str[left] != Str[right] and cnt ==1:
            return 2
        else:
            left+=1
            right-=1
    return cnt
T = int(input())
for _ in range(T):
    Str = input()
    left ,right ,cnt = 0, len(Str)-1, 0
    print(check(left,right, cnt))
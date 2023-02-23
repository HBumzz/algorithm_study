from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

num = deque(map(int, input().split()))
stack = []
i = 1
while num:
    if i == len(num):
        stack.append(-1)
        num.popleft()
        i = 1

    elif num[i] > num[0]:
        stack.append(num[i])
        num.popleft()
        i = 1

    else:
        i += 1
    print(stack)
    print(num)
print(*stack)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = int(input())

lst = []

for time in range(N):
    lst.append(time)
lst.sort()

start = lst[0]
end = lst[-1]
while True:
    c = (start + end)//2
    cnt = 0
    for i in range(len(lst)):
        cnt += c//lst[i]
        
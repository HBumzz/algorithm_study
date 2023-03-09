import sys
sys.stdin = open('input.txt','r')
N = int(input())
lst = []
for i in range(6):
    a, b = map(int, input().split())
    lst.append([a,b])
lst[1
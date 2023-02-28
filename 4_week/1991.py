import sys
sys.stdin = open('input.txt','r')

def preord(n):
    if n != '.':
        print(n, end = '')
        preord(tree[n][0])
        preord(tree[n][1])

def inord(n):
    if n != '.':
        inord(tree[n][0])
        print(n, end = '')
        inord(tree[n][1])

def postord(n):
    if n != '.':
        postord(tree[n][0])
        postord(tree[n][1])
        print(n, end = '')
tree = {}
N = int(input())
for n in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]
preord('A')
print()
inord('A')
print()
postord('A')
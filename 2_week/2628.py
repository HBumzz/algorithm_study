import sys
sys.stdin = open ('input.txt', 'r')
r, l = map(int, input().split())
g = [0, r]
s = [0, l]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0 :
        s.append(b)
    else:
        g.append(b)
g.sort()
s.sort()
g_new = []
s_new = []
for i in range(len(g)-1):
    g_g = g[i+1]-g[i]
    g_new.append(g_g)
for i in range(len(s)-1):
    s_s = s[i+1]-s[i]
    s_new.append(s_s)
print(max(g_new)*max(s_new))

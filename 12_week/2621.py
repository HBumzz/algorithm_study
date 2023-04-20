import sys
sys.stdin =open('input.txt', 'r')

lst1 = []
lst2 = []
for _ in range(5):
    a, b= map(str, input().split())
    b = int(b)
    lst1.append(a)
    lst2.append(b)
# 위부터 찬찬히 1번
ans = 0
st1 = set() # 색깔
st2 = set() # 점수
for i in range(5):
    st1.add(lst1[i])
    st2.add(lst2[i])
if len(st1) == 1: # 1번
    mx = 0
    for i in range(5):
        if lst1[i] > mx:
            mx =lst1[i]
    if mx > ans:
        ans = mx
    ans += 900
if len(st2) == 2: # 2번
    for i in st2:
        if lst2.count(i) == 3:
            if i+800 > ans:
                ans = i+800
if len(st)

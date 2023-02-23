import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [0]*1001
mx_L,mx_H = 0,0
mn_L = 1001
for i in range(N):
    L,H = map(int, input().split())
    lst[L] = H
    if L > mx_L:
        mx_L = L
    if H > mx_H:
        mx_H = H
    if L < mn_L :
        mn_L = L
real_lst = lst[mn_L:mx_L+1]
mx_cnt = real_lst.count(mx_H)
ans = 0
if mx_cnt > 1:
    a = real_lst.index(mx_H)
    b = real_lst[::-1].index(mx_H) # 2
    ans += ((len(real_lst)-b)-a)*mx_H
    left = real_lst[:a]
    right_temp = real_lst[len(real_lst)-b:]
    right = right_temp[::-1]
    mx_left = real_lst[0]
    mx_right = real_lst[-1]
    for i in range(len(left)):
        if left[i] > mx_left:
            mx_left = left[i]
        left[i] = mx_left
        ans+=left[i]
    for i in range(len(right)):
        if right[i] > mx_right:
            mx_right = right[i]
        right[i] = mx_right
        ans+=right[i]
else:
    a = real_lst.index(mx_H)
    ans+=mx_H
    left = real_lst[:a]
    right_temp = real_lst[a+1::]
    right = right_temp[::-1]
    mx_left = real_lst[0]
    mx_right = real_lst[-1]
    for i in range(len(left)):
        if left[i] > mx_left:
            mx_left = left[i]
        left[i] = mx_left
        ans+=left[i]
    for i in range(len(right)):
        if right[i] > mx_right:
            mx_right = right[i]
        right[i] = mx_right
        ans+=right[i]
print(ans)
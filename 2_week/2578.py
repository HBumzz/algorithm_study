import sys
sys.stdin = open('input.txt', 'r')

def Bingo(arr):
    cnt = 0
    for i in range(5):
        if sum(arr[i]) == 0: 
            cnt += 1
    for i in range(5):
        cnt_y = 0 
        for j in range(5):
            if arr[j][i] == 0:
                cnt_y += 1
        if cnt_y == 5:
            cnt += 1
    cnt_d = 0
    for i in range(5): 
        if arr[i][i] == 0:
            cnt_d += 1
    if cnt_d == 5:
        cnt += 1
    cnt_d2 = 0
    for i in range(5): 
        if arr[i][4-i] == 0:
            cnt_d2 += 1
    if cnt_d2 == 5:
        cnt += 1
    return cnt
arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))
lst = []
for i in range(5):
    temp_lst = list(map(int, input().split()))
    for tmp in temp_lst:
        lst.append(tmp) 
for idx, num in enumerate(lst):
    for m in arr: 
        if num in m: 
            m[m.index(num)] = 0 
            break
    result = Bingo(arr)
    if result >= 3:
        print(idx+1)
        break

import sys
from itertools import product
sys.stdin = open('input.txt', 'r')



N, M = map(int, input().split())
# cctv는 몇개 안되니깐 모든 경우의 수 다보자
# 1 -> 4개 2 -> 2개 3->4개 4-> 4개 5-> 1개
dic = {1:[1,2,3,4], 2: [1,2], 3:[1,2,3,4], 4:[1,2,3,4], 5: [1]}

arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            lst.append([i,j,arr[i][j],dic[arr[i][j]]])
products = []
for i, j, cctv_num, s in lst:
    products.append(s)
for combinations in product(products, repeat=len(lst)):
    print(combinations)
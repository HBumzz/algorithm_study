import sys
sys.stdin = open('input.txt','r')
# ACAYKP
# CAPCAK
# ACAK
str1 = input()
str2 = input()
n, m = len(str1), len(str2)
arr = [[0]*(m+1) for _ in range(n+1)]
ans =''
for i in range(n):
    for j in range(m):
        if str1[i] == str2[j]:
            arr[i][j] = arr[i-1][j-1] +1
            print(str1[i], (i,j))
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
for i in range(n):
    print(arr[i])
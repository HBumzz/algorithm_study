# 2차원 배열을 만든다.
str1 = input()
str2 = input()
n, m = len(str1), len(str2)
arr = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if str1[i] == str2[j]:
            arr[i][j] = arr[i-1][j-1] +1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[n-1][m-1])
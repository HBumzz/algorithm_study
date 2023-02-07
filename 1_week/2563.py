# 3,7 -> 3,13 7,17
# 5,2 -> 5,15 2,12
# 15,7 -> 15,25 7,17
arr = [[0]*100 for _ in range(100)]
T = int(input())
for t in range(T):
    a, b = map(int, input().split()) # 3,7
    #arr[6:16][2:12]다 +1
    for i in range(b-1,b+9):
        for j in range(a-1,a+9):
            arr[i][j] +=1
    # 1 넘어서는건 겹쳐지는거 0은 빈공간 -> 2이상인곳을 1로 바꿔줌 or 1이상인 곳을 다 새기
    # 1만 카운트
    hap = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1:
            hap += 1
print(hap)
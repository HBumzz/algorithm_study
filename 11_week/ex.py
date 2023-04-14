arr =[0,1,2,3,4,5,6,7,]
for _ in range(7):
    p = arr.pop(0)
    arr.append(p)  # 방향전환
print(arr)
# [7,0,1,2,3,4,5,6]
arr =[0,1,2,3,4,5,6,7,]

arr.append(arr.pop(0)) # 방향전환
# [1,2,3,4,5,6,7,0]
print(arr)
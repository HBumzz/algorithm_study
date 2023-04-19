arr = [0,1,2,3,4,5,6,7]
arr = arr[7:] + arr[:7]
# for num in range(7):
#     p = arr.pop(0)
#     arr.append(p)
print(arr)
arr = [0,1,2,3,4,5,6,7]
arr.append(arr.pop(0))
print(arr)
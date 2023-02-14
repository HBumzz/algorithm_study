import sys
sys.stdin = open('input.txt', 'r')
num = int(input())
mx = 0
for num2 in range(num+1):
    next_num = num - num2    
    lst = [num, num2, next_num]
    while True:
        next_num = lst[-2]-lst[-1]
        if next_num < 0:
            break
        lst.append(next_num)
    if len(lst) > mx:
        mx = len(lst)
        mx_lst = lst
print(len(mx_lst))
print(*mx_lst)

lst = [1]*2001
for i in range(2,2001):
    if lst[i] :
        for j in range(i,2001,i):
            if i != j:
                lst[j] = 0

N = int(input())
num_lst = list(map(int, input().split()))
if num_lst[0]%2 == 0:
    flag = 1 # 1이면 even[0]이 첫번째 수
else:
    flag = 0 # 0이면 odd[0]이 첫번째 수

odd = []
even = []
for i in range(len(num_lst)):
    if num_lst[i]%2 == 0:
        even.append(num_lst[i])
    else:
        odd.append(num_lst[i])
if len(odd) != len(even):
    ans = -1
    print(ans)
    exit()
v_odd = [0]* (N//2)
v_even = [0]* (N//2)


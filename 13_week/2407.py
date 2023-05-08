n, m = map(int, input().split())
lst = [i for i in range(n)]
lst_a = [(n-i) for i in range(m)]
lst_b = [i for i in range(1,m+1)]
a= b= 1
for num in lst_a:
    a*=num
for num in lst_b:
    b*=num
print(a//b)
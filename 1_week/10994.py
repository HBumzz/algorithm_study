# 2일때 가로5, 세로10 3일때 가로10 세로 20
# 가로 짝수는 다 비어있고, 세로는 양끝에 하나씩만
# 5 2 3 2 5
# 9 2 7 4 5 4 7 2 9
# 13 2 11 4 9 6 7 6 9 4 11 2 13
# 2 3
# 3 5
# 4 7
N = int(input())
for i in range(1, N):
    b = (N-i)*4+1
    print('* '*(i-1) + '*'*b + ' *'*(i-1) ) # 홀수
    print('* '* i + ' '*(b-4) +' *'*i ) # 짝수
print('* '*(N*2-1))
for i in range(N-1,0,-1):
    b = (N-i)*4+1
    print('* '* i + ' '*(b-4) +' *'*i ) # 짝수
    print('* '*(i-1) + '*'*b + ' *'*(i-1) ) # 홀수
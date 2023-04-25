import sys
sys.stdin =open('input.txt', 'r')

card = [list(input().split()) for _ in range(5)] # 그대로 받아주기
numbers = [int(i[1]) for i in card] # 숫자만 따로 int 취해서 list로
cnt_color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0} # 색깔 count를 나타내기 위한 딕셔너리
cnt_num = [0 for _ in range(10)] # 숫자 count를 나타내기 위한 리스트
for i in range(5):
    color, number = card[i][0], int(card[i][1])
    cnt_color[color] += 1
    cnt_num[number] += 1
# 1번 조건
numbers.sort()
ans = 0
if 5 in cnt_color.values() and numbers[0]+1 == numbers[1] and numbers[1]+1 == numbers[2] and numbers[2]+1 == numbers[3] and numbers[3]+1 == numbers[4]:
    ans = max(numbers) + 900
# 2번 조건
elif 4 in cnt_num:
    ans = cnt_num.index(4) + 800
# 3번 조건
elif 3 in cnt_num and 2 in cnt_num:
    ans = cnt_num.index(3)*10 + cnt_num.index(2) + 700
# 4번 조건
elif 5 in cnt_color.values():
    ans = max(numbers) + 600
# 5번 조건
elif numbers[0]+1 == numbers[1] and numbers[1]+1 == numbers[2] and numbers[2]+1 == numbers[3] and numbers[3]+1 == numbers[4]:
    ans = max(numbers) + 500
# 6번 조건
elif 3 in cnt_num:
    ans = cnt_num.index(3) + 400
# 7번 조건
elif cnt_num.count(2) == 2:
    flag = 0
    for i in range(10):
        if not flag and cnt_num[i] == 2:
            ans += i
            flag +=1
        elif flag and cnt_num[i] == 2:
            ans += 10*i
    ans += 300
# 8번 조건
elif cnt_num.count(2) == 1:
    ans = cnt_num.index(2) + 200
else:
    ans = max(numbers) + 100
print(cnt_num)
print(ans)
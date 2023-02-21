icp = {'(':3,'*':2, '+':1, '/':2 ,'-':1}
isp = {'*':2, '+':1, '(':0,'/':2, '-':1}
st = input()
# [1] 중위표기식 => 후위표기식 변환
stk = []
equ = ""
for ch in st:
    if ch.isalpha():  # 숫자인 경우 equ추가
        equ += ch
    else:
        # if ch=='(':     # 무조건 스택에 저장
        #     stk.append(ch)
        # elif ch==')':   # '(' 만날때까지 모두 pop해서 equ추가, '('제거
        if ch == ')':  # '(' 만날때까지 모두 pop해서 equ추가, '('제거
            while stk:
                t = stk.pop()
                if t == '(':  # 괄호연산 완료
                    break
                else:
                    equ += t
        else:
            while stk and icp[ch] <= isp[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)
while stk:
    equ+=stk.pop()
print(equ)
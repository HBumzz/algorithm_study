from itertools import product

def solution(users, emoticons):
    # users [비율, 가격] 가격이상이면 이모티콘 플러스 구매
    # 먼저 이모티콘의 최적의 할인율을 구해야함 -> 가장 많은 이모티콘플러스 가입자가 나오도록
    # users 들의 가격을 넘어서는게 우선
    answer = [-1,-1]
    for emoticon_discounts in product([10,20,30,40], repeat = len(emoticons)):
        # [(10,10), (10,20), (10,30), (10,40), (20,10), (20,20) ...]
        new_users = 0
        total_cost = 0

        for user in users: # user[0] -> 사용자가 구매의향 있는 할인율
            buy_cost = 0
            for i in range(len(emoticon_discounts)):
                if emoticon_discounts[i] >= user[0]: # user[0] 즉 사용자의 할인율을 넘어서면 구입
                    buy_cost += (emoticons[i] * (1-emoticon_discounts[i] / 100)) # 할인된 가격을 buy_cost에 더함
            if buy_cost >= user[1]: # 이모티콘 플러스 가입 가능
                new_users +=1
                buy_cost = 0 # 이모티콘 플러스에 가입하게 되면 2번 목표인 이모티콘 판매액에서 제외
            total_cost += buy_cost
        if new_users > answer[0]: # 이전에 갱신된 answer[0] 보다 new_users가 많다면 1번목표 달성 -> 다시 갱신
            answer[0] = new_users
            answer[1] = total_cost
        elif answer[0] == new_users: # 이전에 갱신된 answer[0]과 같다면 answer[1] 과 현재의 total_cost 중에 max값으로 answer[1] 갱신
            answer[1] = max(answer[1], total_cost)
    return answer
                    
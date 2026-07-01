def solution(enroll, referral, seller, amount):
    answer = []
    
    money = {i:0 for i in enroll}
    ref = {enroll[i]:referral[i] for i in range(len(enroll))}
    
    for idx in range(len(seller)):
        ex = int(amount[idx]*0.1*100)
        me = seller[idx]
        money[me] += amount[idx]*100-ex
        
        while True:
            if ref[me] == "-":
                break
            me = ref[me] # 갱신하기
            origin = ex # 원래 값 저장
            ex = int(origin*0.1) # 다시 0.1떼기
            money[me] += origin - ex # 값 더해줌
            if ex <= 0:
                break
            
    return [money[m] for m in money]
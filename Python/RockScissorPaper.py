import random as rd
#random.ranint() <= X
#rd.randint()    <= O

#가위바위보 게임 작성
code = ["가위", "바위", "보"]
#0 가위, 1 바위, 2 보  input을 숫자로 받음
"""
def sel():
    while(True):
        s = input("가위 :0, 바위:1, 보:2 를 입력해 주세요")
        if(s in ['0','1','2']):
            s = int(s)
            break
    #가위 바위 보 를 입력받는 함수
    #결과를 리턴
    return s
    pass
"""
li = [0,0,0]
def sel():
    #return rd.randint(0,1)
    #print(li)
    total = 0
    for i in li:
        total+=i
    if(total < 10):
        c = rd.randint(0,2)
        return c
    

    l = li[:]
    l.sort()
    
    m_f = li.index(l[0])
    h_f = li.index(l[2])

    #li = [5,9,2]
    #l = [2,5,9]
    

    force = m_f+1
    if(force == 3):
        force = 0
        
    safe = h_f-1
    if(safe == -1):
        safe = 2
        
    s_m = l[2] - total/3
    f_m = total/3 - l[0]
    #print(s_m, f_m)
    if(f_m > s_m):
        c = force
    else:
        c = safe
    return c
    
def com():
    c = rd.randint(0,2)
    #컴퓨터의 가위 바위 보 를 입력받는 함수
    #랜덤 선택
    #결과를 리턴
    return c
    pass

def rcp_res(p1, p2):
    #가위바위보 결과
    #결과 리턴
    #1p 승리시 1, 2p 승리시 -1, 비길시 0
    #0 가위, 1 바위, 2 보  input을 숫자로 받음
    li[p2]+=1
    tmp = p1-p2
    if(tmp == 1 or tmp == -2):
        return 1
    elif(tmp == 0):
        return 0
    else:
        return -1
    

#5번 게임
#유저의 승리/패배/비김 횟수 출력
if __name__ == "__main__":
    w =0
    l =0
    d =0

    print(__name__)

    for i in range(10000):
        user = sel()        
        com_ = com()
        #print("user :",code[user])
        #print("com :",code[com_])

        res = rcp_res(user, com_)

        if(res == 1):
            w +=1
        elif(res == 0):
            d +=1
        elif(res == -1):
            l +=1
            
    print("유저는 %d회 중 %d회 승리 하였으며, %d회 패배하였습니다."%((w+d+l),w, l))

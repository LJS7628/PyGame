import random
def print_menu():
    print("menu".center(10,'='))
    print("1. game start".center(10))
    print("2. game score".center(10))
    print("3. game end".center(10))

def is_strik(answer, user):
    s = 0
    b = 0
    o = 0
    i = 0
    while(i<3):#내가 입력한 걸 하나씩 참조
            tmp = int(user[i])#내가 입력한 값 중 i번째 값
            if(tmp in answer):
                if(i == answer.index(tmp)):
                    s += 1
                    #i <- 내가 선택한 위치
                    #tmp <- 내가 선택한 것
                    #answer.index(tmp)
                    #<- answer에서 내가 선택한것의 위치
                else:
                    b += 1
            else:
                o += 1
            
            i+=1
    return b,s,o

def game_start():
    answer = random.sample([0,1,2,3,4,5,6,7,8,9],3)
    print(answer)
    I = 0
    while(True):#3 스트라이크 까지 반복
        u_in = input("세자리 숫자를 입력하시오 : ")
        b,s,o = is_strik(answer, u_in)
        print("B:%d S:%d O:%d"%(b,s,o))
        I += 1        
        if s == 3:
            break
    print("총",I,"번만에 맞추셨습니다")
    return I

def game_info(sc):
    t = len(sc)
    print("총 플레이 횟수는",t,"회 입니다.")
    print("최근 3경기 결과는")
    for i in sc[-3:]:
        print("%d번째 경기 %d 회"%(t, i))
        t-=1
    s = 0
    for i in sc:
        s += i
    print("평균",s/len(sc),"회 걸렸습니다")

is_do = True
scores=[]
#len(scores) == 총 플레이 횟수
#scores의 총 합 / len(scores) == 평균 걸린 타임
#scores[2], scores[-3:] 가능!
while(is_do):
    print_menu()
    while(True):
        sel = input("메뉴 선택 : (1,2,3 중 입력)")
        if(sel == '1'):
            scores.append(game_start())
            break
        elif(sel =='2'):
            game_info(scores)
            break
        elif(sel=='3'):
            is_do = False
            break
        

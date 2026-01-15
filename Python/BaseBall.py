import random

# 하드코딩
answer = [9,5,4]

# 랜덤 함수 활용
#answer = random.sample([0,1,2,3,4,5,6,7,8,9],3)

I = 0
while(True):#3 스트라이크 까지 반복
    u_in = input("세자리 숫자를 입력하시오 : ")
    #u_in = list(u_in)#[1,2,3] 숫자 배열로 변함
    s = 0
    b = 0
    o = 0

    i = 0
    while(i<3):#내가 입력한 걸 하나씩 참조
        j = 0
        while(j<3):#answer와 하나씩 비교
            if(int(u_in[i]) == answer[j]):#만약 내가입력한게 있다면
                if(i == j):#위치가 같다면
                    s += 1#스트라이크 추가
                    break
                else:#다르면
                    b += 1#볼 추가
                    break
            
            j+=1
        else: #없다면
            o+=1#아웃 추가
        i+=1
    I += 1
    print("B:%d S:%d O:%d"%(b,s,o))
    if s == 3:
        break
print("총",I,"번만에 맞추셨습니다")

info = """
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567 
lee 980908-3a2b0c3
kim 900514-2022023
"""
l = []

info = info.strip('\n')
#맨 앞/뒤 엔터 제거
info_l = info.splitlines()
#줄바꿈 기준 나눠서 저장

for i in info_l:
    tmp = i.split()
    #이름과 주민번호 분리
    f,s = tmp[1].split('-')
    #주민번호 앞/뒤 자리 분리

    if((f+s).isdigit() and len(f)==6 and len(s)==7): #주민번호 규칙이 모두 맞다면
        tmp = i.find('-')
        #뒷자리 위치를 찾은 다음
        l.append(i[:tmp+1]+"*******")
        info = info.replace(i[tmp+1:], "*******")
        #뒷자리를 ******* 으로 바꿔서 저장
    else:
        l.append(i)
        #아니면 그냥 저장
info2 = '\n'.join(l)
#저장된 문자열들을 하나로 합침
#줄 바꿔 가면서
print(info2)
print()
print(info)
    

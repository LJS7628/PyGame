def is_leap(year):
    res = False
    if(year % 400 == 0):
        res = True
    elif(year % 4 == 0 and year % 100 != 0):
        res = True
    return res

def last_day(year, month):
    res = 0
    if(month in [1, 3, 5, 7, 8, 10, 12]):
        res = 31
    elif(month == 2):
        if(is_leap(year)):
            res = 29
        else:
            res = 28
    else:
        res = 30
    return res

# 1. 입력 받기
date = input("날짜를 yyyy/mm/dd 형태로 입력하시오: ")
tmp = date.split('/')

year = int(tmp[0])
month = int(tmp[1])
day = int(tmp[2])

# 2. 윤년 여부 출력
if(is_leap(year)):
    print("윤년입니다")
else:
    print("평년입니다")

print("해당 달의 마지막 날은", last_day(year, month), "일 입니다")

# 3. 기준 날짜 설정 (Today)
td_y = 2020
td_m = 2
td_d = 3

res = 0

# 4. 날짜 차이 계산 로직

# 4-1. 해당 년도들 사이의 전체 날짜 (시작년도+1 ~ 기준년도-1)
for i in range(year + 1, td_y):
    if(is_leap(i)):
        res += 366
    else:
        res += 365

# 4-2. 시작 년도와 기준 년도가 다른 경우
if(year != td_y):
    # 시작한 달의 남은 일수 계산
    res += (last_day(year, month) - day)
    # 시작한 년도의 다음 달부터 12월까지 더하기
    for i in range(month + 1, 13):
        res += last_day(year, i)
    
    # 기준 년도의 1월부터 이전 달까지 더하기
    for i in range(1, td_m):
        res += last_day(td_y, i)
    # 기준 년도의 오늘 일수 더하기
    res += td_d

# 4-3. 시작 년도와 기준 년도가 같은 경우
else:
    if(month == td_m):
        res = td_d - day
    else:
        # 시작한 달의 남은 일수
        res += (last_day(year, month) - day)
        # 사이 달들의 일수
        for i in range(month + 1, td_m):
            res += last_day(year, i)
        # 기준 달의 오늘 일수
        res += td_d

print(f"입력하신 날짜부터 {td_y}/{td_m}/{td_d}까지 총 {res}일 차이납니다.")
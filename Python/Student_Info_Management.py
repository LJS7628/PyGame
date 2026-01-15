#stu_list={"길동":[0,0,10],"기동":[0,0,20], "학수":[0,0,100], "연세":[0,0,99]}
stu_list = {}
try:
    f=open("stu.csv", 'r')
    for i in f:
        #f[0] key
        #f[1:] value
        l = i.strip("\n").split(',')
        l[-1] = int(l[-1])
        stu_list[l[0]] = l[1:]
except Exception as e:
    stu_list={"길동":[0,0,10],"기동":[0,0,20], "학수":[0,0,100], "연세":[0,0,99]}
    print(e, "파일 불러오기 실패")
finally:
    f.close()
    
def print_menu():
    menu = """
1. 학생 등록
2. 학생 점수 등록
3. 학생 정보 출력	
4. 학생 순위순 표시
5. 종료
"""
    print(menu)
    while(True):
        sel = input()
        if(sel in ["1","2","3","4","5"]):
            break
        else:
            print("1-5 까지 숫자로 입력하시오")
        
    return int(sel)#선택지 리턴
    pass
def stu_ins():
    global stu_list
    name = input("name : ")
    loc = input("location : ")
    age = input("age : ")

    stu_list[name] = [loc, age, -1]
    pass
def stu_grade():
    global stu_list
    name = input("점수 등록 할 학생 : ")
    if(not(name in stu_list)):
        print("해당 학생이 없습니다")
        return 
    while(True):
        grade = input("학생 점수 : ")
        if(grade.isdigit()):
            grade = int(grade)
        else:
            print("숫자로 입력해주세요")
            continue

        if(grade <= 100 and grade >=0):
            break
        else:
            print("점수는 0~100 사이 입니다")
    
    stu_list[name][2] = grade

def stu_info():
    name = input("정보 확인을 할 학생 : ")
    print(stu_list[name])
    pass
def stu_rank():
    ls = list(stu_list.items())
    l_ls = len(ls)
    i = 0
    while(i<l_ls):
        j = i+1
        while(j<l_ls):
            if(ls[i][1][2] < ls[j][1][2] ):
                ls[i], ls[j] = ls[j],ls[i]
            j+=1
        i+=1
    for i in ls:
        print(i[0])

while(True):
    sel = print_menu()
    #입력 받음
    
    if(sel == 1):#조건문 직접 채워주세요
        stu_ins()   
    elif(sel == 2):
        stu_grade()
    elif(sel == 3):
        stu_info()
    elif(sel == 4):
        stu_rank()
    elif(sel == 5):
        try:
            f = open("stu.csv", "w")
            for k,v in stu_list.items():
                f.write("%s,%s,%s,%s\n"%(k,v[0],v[1],v[2]))
        except:
            print("파일 저장 실패")
        else:
            break;
        finally:
            f.close()
   

    

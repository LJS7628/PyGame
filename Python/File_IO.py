infos = []
try:
    f = open("info.csv", "r")
    for i in f:
        infos.append(i.strip("\n").split(','))
except Exception as e:
    print(e, "파일 불러오기 실패")
    
def print_menu():
    print("1. 직원정보 추가\n2. 직원정보 출력\n3. 종료")
    return int(input())

if __name__ == "__main__":
    while(True):
        sel = print_menu()
        if(sel == 1):
            name = input("이름")
            age = input("나이")
            loc = input("거주지")
            infos.append([name, age, loc])
        elif(sel == 2):
            print(infos)
        elif(sel == 3):
            try:
                f = open("info.csv", "w")
                for i in infos:
                    f.write("%s,%s,%s\n"%(i[0], i[1], i[2]))
            except:
                print("파일 저장 실패")
            else:
                break
            finally:
                f.close()
        

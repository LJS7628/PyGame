ls = [1,3,42,53,32,2,5,23,34,8]
l_ls = len(ls)
i =0
while(i < l_ls):
    j = i+1
    while(j<l_ls):
        if(ls[i]>ls[j]):
            ls[i],ls[j] = ls[j],ls[i]
            #tmp = ls[i]
            #ls[i] = ls[j]
            #ls[j] = tmp
        j+=1
        #ls[i], ls[j] 비교
        #더 작은게 앞에 오도록 서로 바꿈
    i+=1

print(ls)

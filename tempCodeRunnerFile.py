n=[3,5,1,6,6,8,2,9,5,10]
m=[2,333,1,7,9,4,3]
hashlist = {}
for num in n:
    hashlist[num]+=1
for num in m:
    if num<0 or num>10:
        print("0")
    else:
        print(hashlist[num])
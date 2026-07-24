def duplicate(num):
    num_set=set()
    dupli=[]
    for i in num:
        if i in num_set:
            dupli.append(i)
            print(True)
            print(dupli)
        else:
            num_set.add(i)

    return False

arr=[1,2,3,4,4,5,6,7,8]
duplicate(arr)
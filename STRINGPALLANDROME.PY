def stringpallandrome(s:str) ->bool:
    
    if len(s)<=1:
        return True
    
    if s[0] !=s[-1]:
        return False
    
    return stringpallandrome(s[1:-1])

print(stringpallandrome("racecar"))
print(stringpallandrome("doccof"))
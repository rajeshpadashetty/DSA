def strrev(s):
    if len(s)<=1:
        return s
    else:
        return strrev(s[1:]) + s[0]
    
print(strrev("RAJESH"))   
def is_palandrome(i,s):
  if i>=len(s)//2:
    return True 
  if s[i]!=s[len(s)-i-1]:
    return False
  return is_palandrome(i + 1, s)
str=input("enter the string to check the string is pallandrome or not")
print(is_palandrome(0,str))
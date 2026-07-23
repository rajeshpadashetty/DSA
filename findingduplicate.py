arr = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,8,9,9,9]
unique = set()
for num in arr:
    if num in unique:
      print(num)
    else:
       unique.add(num)
print(unique)
with open('digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())
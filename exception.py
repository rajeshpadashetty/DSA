file_name="digits.txt"
try:
     with open(file_name) as file_object:
       content = file_object.read()
       print(content)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")

except PermissionError:
    print(f"Permission denied to read the file '{file_name}'")
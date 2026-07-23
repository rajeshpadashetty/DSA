file_name="digits.txt"

try:
   with open("digits.txt") as file_object:

    for line in file_object:
        print(line.rstrip())
    
except FileNotFoundError:
   print(f"File '{file_name}' not found.")

except PermissionError:
    print(f"Permission denied to read the file '{file_name}'")
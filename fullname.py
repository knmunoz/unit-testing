# generates a full name when provided first and last name as inputs

def fullname(f, l):
    full_name = f + " " + l
    return full_name.title()

first = input("Enter first name: ")
if first == '':
    raise ValueError("empty name")
last = input("Enter last name: ")
if last == '':
    raise ValueError("empty name")

print("Full name: ", fullname(first, last))
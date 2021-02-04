# generates a full name when provided first and last name as inputs

def fullname(f, l):
    return f + " " + l

first = input("Enter first name: ")
last = input("Enter last name: ")

print("Full name: ", fullname(first, last))
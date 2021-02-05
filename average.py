# calculate the average of elements in a list

def avg(l):
    if len(l) == 0:
        raise ValueError("list is empty")
    else:
        return sum(l) / len(l)

lst = []
count = 1

n = int(input("Enter number of elements in list: "))

for i in range (0, n):
    element = int(input("Element %d: " %count))
    if type(element) not in [int, float]:
        raise TypeError("list element must be valid int or float")
    else:
        lst.append(element)
        count += 1

average = avg(lst)

print("List: ", lst)
print("Average of elements in list: %.2f" %average)
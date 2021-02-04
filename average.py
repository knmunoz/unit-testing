# calculate the average of elements in a list

def avg(l):
    return sum(l) / len(l)

lst = []
count = 1

n = int(input("Enter number of elements in list: "))

for i in range (0, n):
    element = int(input("Element %d: " %count))
    lst.append(element)
    count += 1

average = avg(lst)

print("List: ", lst)
print("Average of elements in list: %.2f" %average)
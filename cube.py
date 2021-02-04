# calculate the volume of a cube

def vol(l):
    return l * l * l

length = float(input("Enter the length of any side of the cube: "))

volume = vol(length)

print("Volume of the cube: %.2f" %volume)
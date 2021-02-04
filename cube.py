# calculate the volume of a cube

def vol(l):
    if type(l) not in [int, float]:
        raise TypeError
    elif l < 0:
        raise ValueError
    else:
        return l * l * l

length = float(input("Enter the length of any side of the cube: "))

volume = vol(length)

print("Volume of the cube: %.2f" %volume)
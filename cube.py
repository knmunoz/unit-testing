# calculate the volume of a cube

def vol(l):
    if type(l) not in [int, float]:
        raise TypeError("length must be a valid int or float")
    elif l < 0:
        raise ValueError("length cannot be less than zero")
    else:
        return l * l * l

length = float(input("Enter the length of any side of the cube: "))

volume = vol(length)

print("Volume of the cube: %.2f" %volume)
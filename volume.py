import math


def volume():
    radius = input("Enter radius of cylinder (cm): ")
    height = input("Enter height of cylinder (cm): ")

    volume = math.pi * (float(radius) * float(radius)) * float(height)

    volume = "The volume of a cylinder with a radius of {} and a height of {} is {} cm^3".format(
        radius, height, round(volume, 3)
    )

    return volume


print(volume())

print("\ndone")

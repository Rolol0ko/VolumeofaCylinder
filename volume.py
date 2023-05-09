import math


def volume_cylinder(height: float, radius: float) -> float:
    volume = math.pi * pow(radius, 2) * height

    return volume


def main() -> None:
    user_height = float(input("Enter the height of the cylinder (cm): "))
    user_radius = float(input("Enter the radius of the cylinder (cm): "))

    print("")

    volume = volume_cylinder(user_height, user_radius)

    print(
        f"The volume of a cylinder with a radius of {user_radius} and a height of {user_height} is {round(volume, 3)} cm^3"
    )
    print("\nDone.")


if __name__ == "__main__":
    main()

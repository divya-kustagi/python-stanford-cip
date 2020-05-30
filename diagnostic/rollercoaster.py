"""
rollercoaster.py

Program for 'Can I Ride the Rollercoaster':
If height is < 1 meter or > 2 meters, can't ride.
If 1 meter <= height <= 2 meters, can ride!
"""


def main():
    user_height = float(input("Enter height in meters: "))
    if (user_height < 1) or (user_height > 2):
        print("You can't ride the roller coaster.")
    else:
        print("You can ride the roller coaster.")


if __name__ == "__main__":
    main()

import math
from datetime import datetime

# Get input from the user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))

diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Round the volume to 2 decimal places
volume_rounded = round(volume, 2)

# Print the result
print(f"The approximate volume is {volume_rounded} liters")

# Get the current date
current_date = datetime.now()

# Open the volumes.txt file for appending and write the data
with open("volumes.txt", "at") as volumes_file:
    # Write the data in the specified format
    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}", 
          file=volumes_file)
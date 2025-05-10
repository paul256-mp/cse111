import math
from datetime import datetime

# Get input from the user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
volume_rounded = round(volume, 2)

# Print the result
print(f"\nThe approximate volume is {volume_rounded} liters")

# Determine tire price based on dimensions
if width == 185 and aspect_ratio == 65 and diameter == 15:
    price = 89.99
elif width == 205 and aspect_ratio == 55 and diameter == 16:
    price = 112.99
elif width == 225 and aspect_ratio == 60 and diameter == 17:
    price = 149.99
elif width == 245 and aspect_ratio == 45 and diameter == 18:
    price = 189.99
elif width == 265 and aspect_ratio == 70 and diameter == 16:
    price = 219.99
else:
    price = None

if price is not None:
    print(f"Price for {width}/{aspect_ratio}R{diameter}: ${price:.2f}")
else:
    print("No specific pricing found for these dimensions.")

# Ask if user wants to buy tires
buy_tires = input("\nDo you want to buy tires with these dimensions? (yes/no): ").lower()

phone_number = ""
if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")
    print("Thank you! We'll contact you soon.")

# Get current date and prepare data for file
current_date = datetime.now()
data_to_write = f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume_rounded}"

# Add price and phone number if available
if price is not None:
    data_to_write += f", ${price:.2f}"
if phone_number:
    data_to_write += f", {phone_number}"

# Write to volumes.txt file
with open("volumes.txt", "at") as volumes_file:
    print(data_to_write, file=volumes_file)
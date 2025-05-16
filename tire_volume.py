import math
from datetime import datetime
width =  float(input("Enter the width of the tire in mm(ex 205 )"))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60) "))
diameter = float(input("Enter the diameter of the tire in inches (ex 15) "))

Volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print("The volume of the tire is: ", Volume, "liters")
#finding the price of the tire
input_price = float(input("please enter the width, aspectratio, diameter and volume. "))
if width == 205 and aspect_ratio == 60 and diameter == 15 and Volume == 0.5:
    price = 100
elif width == 215 and aspect_ratio == 65 and diameter == 16 and Volume == 0.6:
    price = 120
elif width == 225 and aspect_ratio == 70 and diameter == 17 and Volume == 0.7: 
    price = 140
elif width == 235 and aspect_ratio == 75 and diameter == 18 and Volume == 0.8:
    price = 160
else:
    print("The price is not available for this width.")
    price = 0

 
 #asking the user if she wants to buy
telphone_number =""
buy = input("Do you want to buy the tire? (yes/no) ")
if buy.lower() == "yes":
    telphone_number = input("Please enter your telephone number: ")
    print(f"Thank you for your order! The price of the tire is {price} and we will contact you at {telphone_number}.")
else:
    print("Thank you for your interest! If you have any questions, feel free to ask.")


# Get the current date and time
current_datetime = datetime.now()
date_to_write = (f'{current_datetime.strftime("%Y-%m-%d %H:%M:%S")}, width: {width}, aspect_ratio: {aspect_ratio}, diameter: {diameter}, volume: {Volume}\n')
# Open the file in append mode and write the date and volume

with open("tire_volume.txt", "at") as volume_tire:
  print( date_to_write, file=volume_tire)
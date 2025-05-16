import math


def main():
  name = "1 picnic "
  radius = 6.83
  height = 10.18
  volume = cone_volume(radius, height)
  area = cone_surface_area(radius, height)
  ff= volume/area
  print(f"The volume of the {name} is: , volume={volume:.2f} and area= {area:.2f} efficiency={ff:.2f}")

  name = "tall "
  radius = 7.78
  height = 11.91
  ff= cone_efficiency(name,radius, height)

def cone_efficiency(name,radius, height):  
    volume = cone_volume(radius, height)
    area = cone_surface_area(radius, height)
    ff = volume / area
    print(f"The volume of the {name} is: , volume={volume:.2f} and area= {area:.2f} efficiency={ff:.2f}")


def cone_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def cone_surface_area(radius, height):
   area= 2*math.pi*radius*(radius + height)
   return area
main()
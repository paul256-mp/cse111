def main():
  # Get an odometer value in U.S. miles from the user.
  start_miles =float(input("Enter the starting odometer value in U.S. miles: "))

  # Get another odometer value in U.S. miles from the user.
  end_miles= float(input("Enter the ending odometer value in U.S. miles: "))

  # Get a fuel amount in U.S. gallons from the user.
  amount_gallon = float(input("Enter the amount of fuel used in U.S. gallons: "))

  # Call the compute_miles_per_gallon function and store
  miles_per_gallon = compute_miles_per_gallon(start_miles, end_miles, amount_gallon)
   # the result in a variable named mpg.
  print(f"Your vehicle's fuel efficiency is {miles_per_gallon:.2f} miles per gallon.")

  # Call the lp100k_from_mpg function to convert the
  lp100k = 235.215 / miles_per_gallon

  # miles per gallon to liters per 100 kilometers and


  # store the result in a variable named lp100k.
  print(f"Your vehicle's fuel efficiency is {lp100k:.2f} liters per 100 kilometers.")
  # Display the results for the user to see.
pass
  
  # Remove this misplaced calculation
def compute_miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  return (end_miles - start_miles) / amount_gallons
  """
  return (end_miles - start_miles) / amount_gallons
def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
# Call the main function so that

main()
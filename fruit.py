
def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

  fruit_list.reverse()
  print(f"reversed: {fruit_list}")

  fruit_list.append("orange")
  print(f"appended: {fruit_list}")

  
  fruit_list.insert(2, "cherry")
  print(f"inserted: {fruit_list}")

  fruit_list.remove("banana")
  print(f"removed: {fruit_list}")

  fruit_list.pop(4)
  print(f"popped: {fruit_list}")

  fruit_list.sort() 
  print(f"sorted: {fruit_list}")

  fruit_list.clear()
  print(f"cleared: {fruit_list}")
  


if __name__ == "__main__":
    main()
  
  # Sort the list in alphabetical order and print it.
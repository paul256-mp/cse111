#practicing how to create adictionary in python
book={'name':'neph','chapter':1}
print(book)
print(book['name'])
# Adding a new key-value pair to the dictionary
book['name']='nephi'
print(book)
# Adding another key-value pa
book['stdwork']= 'book of mormon'
print(book)
del[book['stdwork']]
print(book)


def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)
    print()
    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]
        print(color)
        print()
# Call main to start this program.

def main():
    sum = 0
    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number
    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")
# Call main to start this program.



def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3
    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    total_friut_amount = 0.0
    # Use a for loop to iterate through the inner lists.
    for inner_list in apple_tree_data:
      fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
      print(fruit_amount)
      total_friut_amount += fruit_amount
      print(f"total Fruit amount: {total_friut_amount:.1f} ")

if __name__ == "__main__":
    main()

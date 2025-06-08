import csv
import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary.
    
    Parameters:
        filename: the name of the CSV file to read
        key_column_index: the index of the column to use as dictionary keys
    Returns:
        A dictionary with contents of the CSV file
    """
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        # Skip header row
        next(reader)
        for row in reader:
            if len(row) > 0:  # Skip empty rows
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

def main():
    # Read product data into dictionary (product number as key)
    products_dict = read_dictionary('products.csv', 0)
    
    print("All Store Products:")
    print(products_dict)
    print("\nCustomer Order Receipt:")
    
    # Process request.csv line by line (not as dictionary)
    with open('request.csv', 'rt') as csv_file:
        reader = csv.reader(csv_file)
        # Skip header row
        next(reader)
        
        # Initialize order total
        total_quantity = 0
        subtotal = 0.0
        
        for row in reader:
            if len(row) == 0:  # Skip empty rows
                continue
                
            try:
                # Get product number and quantity from request
                product_num = row[0]
                quantity = int(row[1])
                
                # Look up product details
                product = products_dict[product_num]
                name = product[1]
                price = float(product[2])
                
                # Calculate line total
                line_total = quantity * price
                
                # Update order totals
                total_quantity += quantity
                subtotal += line_total
                
                # Print item details
                print(f"{name}: {quantity} @ ${price:.2f} = ${line_total:.2f}")
                
            except KeyError:
                print(f"Warning: Product {product_num} not found in catalog")
            except ValueError:
                print(f"Warning: Invalid quantity for product {product_num}")
    
    # Calculate sales tax (6%) and total
    tax_rate = 0.06
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax
    
    # Print receipt summary
    print("\nOrder Summary:")
    print(f"Number of Items: {total_quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for your order!")

    #print the cuurrent date and time
    from datetime import datetime
    current_time = datetime.now()
    print(f"Order Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()


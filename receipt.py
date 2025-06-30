import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary."""
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

def calculate_discount(product_num, quantity, price):
    """Calculate discount for BOGO half-off on D083."""
    if product_num == "D083" and quantity >= 1:
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2
        return (full_price_items * price) + (half_price_items * price * 0.5)
    return quantity * price

def get_new_years_countdown():
    """Calculate days until New Year's sale."""
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    delta = new_year - today
    return delta.days

def generate_coupon(ordered_products, products_dict):
    """Generate a coupon for a random ordered product."""
    import random
    if ordered_products:
        product_num = random.choice(list(ordered_products.keys()))
        product = products_dict[product_num]
        discount = round(float(product[2]) * 0.2, 2)  # 20% discount
        return f"${discount:.2f} off next {product[1]}"
    return "$1.00 off any item"

def main():
    products_dict = read_dictionary('products.csv', 0)
    
    print("\n=== GROCERY STORE RECEIPT ===")
    print("\nOrder Details:")
    
    ordered_products = {}
    total_quantity = 0
    subtotal = 0.0
    
    with open('request.csv', 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        
        for row in reader:
            if len(row) == 0:
                continue
                
            try:
                product_num = row[0]
                quantity = int(row[1])
                product = products_dict[product_num]
                name = product[1]
                price = float(product[2])
                
                # Track ordered products for coupon
                if product_num in ordered_products:
                    ordered_products[product_num] += quantity
                else:
                    ordered_products[product_num] = quantity
                
                # Apply BOGO discount for D083
                if product_num == "D083":
                    line_total = calculate_discount(product_num, quantity, price)
                    discount_msg = " (BOGO 50% off applied)" if quantity > 1 else ""
                else:
                    line_total = quantity * price
                    discount_msg = ""
                
                subtotal += line_total
                total_quantity += quantity
                
                print(f"{name}: {quantity} @ ${price:.2f}{discount_msg} = ${line_total:.2f}")
                
            except (KeyError, ValueError) as e:
                print(f"! Error processing item: {row}")

    # Calculate totals
    tax_rate = 0.06
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax
    
    # Print summary
    print("\n=== ORDER SUMMARY ===")
    print(f"Items: {total_quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    print(f"TOTAL: ${total:.2f}")
    
    # Bonus features
    print("\n=== SPECIAL OFFERS ===")
    
    # New Year's countdown
    days_left = get_new_years_countdown()
    print(f"⏳ Only {days_left} days until our New Year's Sale begins!")
    
    # Return policy
    return_date = datetime.now() + timedelta(days=30)
    print(f"🔄 Return by: {return_date.strftime('%b %d')} before 9:00 PM")
    
    # Coupon
    coupon = generate_coupon(ordered_products, products_dict)
    print(f"🎟️ Your coupon: {coupon}")

    #date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    print(f"\nReceipt generated on: {current_time}")
    
    print("\nThank you for shopping with us!")


if __name__ == "__main__":
    main()
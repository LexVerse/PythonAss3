# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompting the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(price, discount_percent)

# Displaying the result
if final_price < price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {price:.2f}")

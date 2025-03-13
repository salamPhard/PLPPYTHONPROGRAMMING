def calculate_discount(price, discount_percent):
    calcDiscount = discount_percent/100
    final_price = price - (calcDiscount * price)
    if discount_percent < 20:
        return price #return the original price
    else:
        return final_price #apply discount and return discounted price

price = int(input("Enter the price of the item"))
discount = float(input("Enter the discount percentage"))
print(calculate_discount(price, discount))
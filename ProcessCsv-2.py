import csv

def calc_sales(coupon: str, discount_amount: float, disc: float = .05) -> float:
    """Calculate total sales amount based off amount of discount given on the order"""
    sales_total = 0.00
    order_sale_price = discount_amount / disc
    sales_total += order_sale_price
    print('Total referral sales for', coupon + ' is: ', round(sales_total, 2))
    coupon_payouts(coupon, sales_total)


def coupon_payouts(coupon: str, sales_total: float, commrate: float = .10)-> float:
    """Calculate the commission rate"""
    print('Commission payout for', coupon, 'is $' + str(round(sales_total * commrate, 2)), '\n')

# Open and read each row from the spreadsheet into memory
with open('Coupon_Usage_Tracking-2.csv', 'r') as purchases:
    csv_purchases = csv.reader(purchases)

    # Initialize working variables
    c_total = 0.00
    c_name = ''
    c_usage = 0

    # Read each row from the spreadsheet loaded into csv_purchases
    for cp in csv_purchases:

        if c_name != cp[1]:                            # Block ensures that all sales for each coupon are totaled
            print(c_name, 'used ' + str(c_usage) + 'x for a total customer discount of $' + str(round(c_total, 2)))
            calc_sales(c_name, c_total)
            c_name = cp[1]
            c_total = 0.00                             # Resets working variable once coupon value changes
            c_usage = 0

        c_total += float(cp[2])
        c_usage += 1


# Prints the last row
print(c_name, 'used ' + str(c_usage) + 'x for a total discount of $' + str(round(c_total, 2)))
calc_sales(c_name, c_total)



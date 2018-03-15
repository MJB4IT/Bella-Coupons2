
total_payout = 0.00

def calc_sales(disc: float = .05)-> float:
    """Calculate total sales amount based off amount of discount given on the order"""
    sales_total = 0.00
    discount_amount = 27.89
    order_sale_price = discount_amount / disc
    sales_total += order_sale_price
    print(round(sales_total, 2))
    return sales_total

def coupon_payouts(coupon, commrate: float = .10)-> float:
    """Calculate the commission rate"""
    sales = calc_sales(.05)
    print(coupon, '$' + str(round(sales * commrate, 2)))


coupon_payouts('NJDJK', .10)


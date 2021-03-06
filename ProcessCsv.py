import csv

# Open and read each row from the spreadsheet into memory
purchases = open('Coupon_Usage_Tracking-2.csv', 'r')
csv_purchases = csv.reader(purchases)

# Initialize working variables
c_total = 0.00
c_name = ''
c_usage = 0

# Read each row from the spreadsheet loaded into csv_purchases
for cp in csv_purchases:

    if c_name != cp[1]:                            # Block ensures that all sales for each coupon are totaled
        print(c_name, 'used ' + str(c_usage) + 'x $' + str(round(c_total, 2)))
        c_name = cp[1]
        c_total = 0.00                             # Resets working variable once coupon value changes
        c_usage = 0
    c_total += float(cp[2])
    c_usage += 1

# Prints the last row
print(c_name, '$' + str(round(c_total, 2)))

# Close the file
purchases.close()
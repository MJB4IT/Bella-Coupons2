import csv

purchases = open('Coupon_Usage_Tracking-2.csv', 'r')
csv_purchases = csv.reader(purchases)

c_total = 0.00
c_name = ''
for cp in csv_purchases:

    if c_name != cp[1]:
        print(c_name, '$' + str(round(c_total, 2)))
        c_name = cp[1]
        c_total = 0.00
    c_total += float(cp[2])

print(c_name, '$' + str(round(c_total, 2)))
purchases.close()

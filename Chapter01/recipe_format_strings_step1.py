data = [
    (1000, 10),
    (2000, 17),
    (1003, 24),
    (2500, -170)
]

#Print the header for reference
print('REVENUE | PROFIT | PERCENT')

TEMPLATE = '{{revenue:>7,}} | {profit:>+6} | {percent:>7.2%}'

for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit= profit, percent= profit/revenue)
    print(row)

print(f"Test of curly brackets = {{{revenue}}}")
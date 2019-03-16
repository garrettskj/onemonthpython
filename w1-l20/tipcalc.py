#/usr/bin/python3

# ask the user for the total amount
str_total_bill = (input("Input total bill amount: "))

# replace any dollar signs with nothing & convert to float
total_bill = float(str_total_bill.replace("$",""))

#print the header
print(f"\n" * 2)
print(f"Total Bill: ${total_bill:.2f}")
print("-" * 20)
print("Recommended Tip Amounts:")

# loop through each percentage and print out recommended totals.
for percent in (15,18,20):
	print(f"{percent}% of ${total_bill:.2f}: ${(total_bill * (percent/100)):.2f}")

print(f"\n" * 2)

#2. You and your partner are planning a trip, and you want to track expenses.
#Create two dictionaries, one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
my_expenses = {
    "Hotel": 1500,
    "Food": 1000,
    "Transportation": 600,
    "Attractions": 450,
    "Miscellaneous": 300
}
partner_expense = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 800,
    "Miscellaneous": 150
}
total_expense = sum(my_expenses.values())
partner_total_expenses = sum(partner_expense.values())
print(f"My total expenses: {total_expense}")
print(f"My partner's total expenses: {partner_total_expenses}")

if total_expense > partner_total_expenses:
    print("I've spent more money overall.")
elif total_expense < partner_total_expenses:
    print("My partner has spent more money overall.")
else:
    print("Both of us spent the same amount.")
print("\nSignificant differences in the expense between me and my partner is:")
for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expense[category])
    if difference >= 100:
        print(f"Category: {category}, Difference: {difference}")
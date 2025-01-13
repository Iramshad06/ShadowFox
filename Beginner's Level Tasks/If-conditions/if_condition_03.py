#3. Write a program to check if two cities belong to the same country.
#Ask the user to enter two cities and print whether they belong to the same country or not.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
first_city = input("Enter the first city: ")
second_city = input("Enter the second city: ")
if first_city in Australia:
    country1 = "Australia"
elif first_city in UAE:
    country1 = "UAE"
elif first_city in India:
    country1 = "India"
else:
    print("City not found")

if second_city in Australia:
    country2 = "Australia"
elif second_city in UAE:
    country2 = "UAE"
elif second_city in India:
    country2 = "India"
else:
    print("City not found")
    
if country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")

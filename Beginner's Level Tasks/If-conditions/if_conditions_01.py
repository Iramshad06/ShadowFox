#1. Write a program to determine the BMI Category based on user input.
#Ask the user to: Enter height in meters, Enter weight in kilograms
#Calculate BMI using the formula: BMI = weight / (height)**2
Height=float(input("Enter the height in meters:"))
Weight=float(input("Enter the weight in kilograms:"))
BMI=Weight/(Height**2)
print("The value of BMI is: ",BMI)
if BMI >=30:
    print("Obesity")
elif 25<=BMI<=29:
    print("Overweight")
elif 18.5<=BMI<25:
    print("Normal")
else:
    print("Underweight")

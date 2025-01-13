#2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
#Write a program that: Asks you to perform 10 jumping jacks at a time. After each set, it asks, "Are you tired?"
#If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
#If you reply "yes" or "y," it should break and print, "You completed a total of jumping jacks."
jumpingjacks_goal = 100
completed = 0
set_size = 10

while completed < jumpingjacks_goal:
    completed += set_size
    print(f"You completed {completed} jumping jacks.")  

    if completed == jumpingjacks_goal:
        print("Congratulations! You completed the workout.")
        break 

    value = input("Are you tired?: ").lower()  
    if value in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    elif value in ["no", "n"]:
        remaining = jumpingjacks_goal - completed
        print(f"{remaining} jumping jacks remaining.\n")
    else:
        print("Invalid input. Please answer with yes or no.")

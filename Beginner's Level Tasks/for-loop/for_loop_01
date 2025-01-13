#1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times).
#Count and print the following statistics:How many times you rolled a 6, How many times you rolled a 1, How many times you rolled two 6s in a row?
import random
max_num_rolls = 20  
count_of_6 = 0     
count_of_1 = 0     
count_of_two_6s_in_row = 0  
previous_roll = None 
for i in range(max_num_rolls):
    value = random.randint(1, 6)
    print(f"Roll {i + 1}: {value}")
    if value == 6:
        count_of_6 += 1
        if previous_roll == 6:
            count_of_two_6s_in_row += 1
    elif value == 1:
        count_of_1 += 1
    previous_roll = value  
print(f"Number of times 6 was rolled: {count_of_6}")
print(f"Number of times 1 was rolled: {count_of_1}")
print(f"Number of times two 6s were rolled in a row: {count_of_two_6s_in_row}")

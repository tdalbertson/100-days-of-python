"""
100 Days of Python Day 2 Project
Tip Calculator
"""

def tip_switcher(tip):
    switcher = {
        10: 0.10,
        12: 0.12,
        15: 0.15
    }
    
    return switcher.get(tip, "default")

print("Welcome to the Tip Calculator!")

bill_total = float(input("What was the total bill? "))

number_to_split = int(input("How many people to split the bill? "))

desired_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_percentage = tip_switcher(desired_tip)

total_w_tip = (bill_total * tip_percentage) + bill_total
split_total = total_w_tip / number_to_split

print(f"Each person should pay: {split_total}")

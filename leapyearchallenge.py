# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# Solution using a Boolean
# leap_year = None

# if year % 4 == 0:
#     leap_year = True
#     if year % 100 == 0:
#         leap_year = False
#         if year % 400 == 0:
#             leap_year = True

# if leap_year == True:
#     print('Leap year.')
# else:
#     print('Not leap year.')

# Instructor Solution
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')        

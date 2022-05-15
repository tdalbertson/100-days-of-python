# Day 9 Project - Secret Auction Program

from ctypes import py_object
import os
from unicodedata import name
import pyinputplus as pyip
from art import logo

# Function Definitions

# To clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def getBidderNameAndBid():
    name = pyip.inputStr(prompt='What is your name?: ')
    bid = pyip.inputNum(prompt='What is your bid?: $')
    
    return name, bid

# Main Function

auction_name_and_price = dict()

print(logo)
print("Welcome to the secret auction program.")

# Gather bidder info
while(True):
    bidder_name, auction_bid = getBidderNameAndBid()
    auction_name_and_price[bidder_name] = auction_bid
    other_bidder = pyip.inputYesNo(prompt='Are there any other bidders? Type \'yes\' or \'no\'. ')
    
    if other_bidder == 'yes':
        clearConsole()
        continue
    else:
        break


# Compare bids and set winner    
auction_winner = ''    
highest_bid = 0    
for auction_name, auction_bid in auction_name_and_price.items(): # Check each item using tuple unpacking
    if auction_bid > highest_bid:
        highest_bid = auction_bid
        auction_winner = auction_name
        
# Print final results        
clearConsole()
print(f'The winner is {auction_winner} with a bid of ${auction_bid}.')

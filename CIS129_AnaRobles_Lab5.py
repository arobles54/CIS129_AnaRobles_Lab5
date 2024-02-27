# Lab 5 The Bottle Return Program
# Author: Ana Robles
# Date: 02/26/2024
# Description: This program calculates the total number of bottles collected for the week and the total payout.

total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0.0
keep_going = "y"

while keep_going.lower() == "y":
    total_bottles = 0
    total_payout = 0.0

    print("Total Bottles collected for the week:", total_bottles)
    print("Total Payout for the week: $", total_payout)

    keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

NBR_OF_DAYS = 7
total_bottles = 0
today_bottles = 0
counter = 0

while counter < NBR_OF_DAYS:
    today_bottles = int(input(f"Enter number of bottles returned for day #{counter + 1}: "))
    total_bottles += today_bottles
    counter += 1

PAYOUT_PER_BOTTLE = 0.10
total_payout = total_bottles * PAYOUT_PER_BOTTLE

print("The total number of bottles collected is", total_bottles)
print("The total paid out is $", total_payout)

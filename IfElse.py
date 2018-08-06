#! /bin/python3
# Heather Lemon 7/29/2018
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird; otherwise, print Not Weird.
N = round(int(float(input())))

def numbers(n):
    if n % 2 == 0:
       if 2 <= n <= 5:
           print("Not Weird")
       elif 6 <= n <= 20:
           print("Weird")
       elif n > 20:
           print("Not Weird")
    else:
        print("Weird")

if __name__:
    numbers(N)
#!/bin/bash
# Heather Lemon 7/29/2018
# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# The first line contains the first integer, . The second line contains the second integer

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b


if __name__ == '__main__':
    a = round(int(float((input()))))
    b = round(int(float((input()))))

    print(addition(a,b))
    print(subtraction(a,b))
    print(multiply(a,b))



#!/usr/bin/python

# In this challenge, we practice calculating standard deviation.
#
# Task
# Given an array x, of x integers, calculate and print the standard deviation.
# Your answer should be in decimal form, rounded to a scale of
# decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.
#
# Input Format
# The first line contains an integer ,i , denoting the number of elements in the array.
# The second line contains space-separated integers, x y z
# describing the respective elements of the array.
#
# Constraints
# 5 <= N >= 100
# , where x(i) is the element of array X.
# Output Format
#
# Print the standard deviation on a new line, rounded to a
# scale of 0.1 decimal place (i.e.,  format).

import statistics
import math

def squaredDistance(inputList, mean):
    sum = 0
    for i in inputList:
        num = ((int(i) - mean)**2)
        sum = sum + num
    return sum

# find the mean of the array
def findMean(array):
    return statistics.mean(array)

def squareRootOfSumOverLengthList(result, num):
    return math.sqrt(result/num)


if __name__ == '__main__':
    input()
    inputListStr = input()
    inputList = inputListStr.split(" ")
    num_array = list()
    for i in inputList:
        num_array.append(int(i))
    mean = findMean(num_array)
    result = squaredDistance(inputList, mean)
    final = squareRootOfSumOverLengthList(result, len(inputList))
    print(round(final,1))

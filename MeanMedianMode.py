#!/bin/bash
# Print  lines of output in the following order:
#
# Print the mean on a new line, to a scale of  decimal place (i.e., , ).
# Print the median on a new line, to a scale of  decimal place (i.e., , ).
# Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
from scipy import stats


def mean(a, b):
    return sum(b) / a


def median(a, b):
    b.sort()
    if a % 2 == 0:
        middle = int((len(b)) / 2)
        return (b[middle] + b[middle - 1]) / 2

    else:
        return (b[a]) / 2


def mode(b):
    b.sort()
    return stats.mode(b)


if __name__ == '__main__':
    # sample input
    # a = 10
    # b = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
    numInput = input()
    inputListStr = input()
    inputList = inputListStr.split(" ")
    num_array = list()
    for i in inputList:
        num_array.append(int(i))
    print(mean(int(numInput), num_array))
    print(median(int(numInput), num_array))
    modeResult = mode(num_array)
    print(int(modeResult[0]))

#!/bin/bash

def intDivide(a,b):
    return a // b

def floatDivide(a,b):
    return a / b

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(intDivide(a,b))
    print(floatDivide(a,b))
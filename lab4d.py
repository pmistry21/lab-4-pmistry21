#!/usr/bin/env python3
# Strings 1

# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024
# Date: 2024/10/11


str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(f5):
    # Place code here - refer to function specifics in section below
    return f5[:5]

def last_seven(l7):
    # Place code here - refer to function specifics in section below
    return l7[-7:]

def middle_number(mn):
    # Place code here - refer to function specifics in section below
    str_mn = str(mn)
    return str_mn[1:3]

def first_three_last_three(f3, l3):
    # Place code here - refer to function specifics in section below
    return f3[:3] + l3[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
#!/usr/bin/env python3


def find_error(input_file='input_file.txt'):
    target = 2020
    d = dict()
    with open(input_file, 'r') as expense_report:
        for expense in expense_report:
            num = int(expense)
            if target - num in d:
                return (target - num) * num
            d[num] = num

        return 0

print(find_error())

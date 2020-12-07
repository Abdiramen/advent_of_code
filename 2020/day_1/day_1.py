#!/usr/bin/env python3

'''
  time complexity n
'''
def find_terms(nums, target=2020):
    d = dict()
    for num in nums:
        if target - num in d:
            return (target - num), num
        d[num] = num
    return 0, 0

'''
  time complexity n
'''
def part_1(nums):
    a, b = find_terms(nums)
    return a * b

'''
  time complexity n*2, memory and time hog
'''
def part_2(nums, target=2020):
    for i, v in enumerate(nums):
        a, b = find_terms(nums[:i] + nums[i+1:], target - v)
        if a + b != 0:
            return v * a * b

with open('input_file.txt', 'r') as expense_report:
    expenses = [int(expense) for expense in expense_report]
    print(part_1(expenses))
    print(part_2(expenses))

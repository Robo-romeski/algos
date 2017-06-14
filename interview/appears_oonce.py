"""
Find the element that appears once
Given an array where every element occurs three times, except one element 
which occurs only once. Find the element that occurs once. 
Examples: 
Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
Output: 2
Idea: Keep hash map of elements ocured - after third time occurance - remove element 
form hash map - the only one that is left in HM is the one we are looking for 
- if there are more than one element in HM - input was wrong 
- one check we can do at the begining - if len(array) %3 == 0 - we know it is wrong input
and len has to be at least 4
"""

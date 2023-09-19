# re.search('expresion', 'text_to_search')
# returns a True/False depending on whether the data string matches the regular expresion

# re.findall('expresion', 'text_to_search')
# extracs the matching strngs, returns a list of the matches
# By default, greedy matching is used, it means it matches the largest possible string
# We han use ? in our regular expresions to avoid greedy behaivor
# We can use () to extrac only a porting of the matching characteres

"""
^       Matches the beginning of a line
$       Matches the end of the line
.       Matches any character
\s      Matches whitespace
\S      Matches any non-whitespace character
*       Repeats a character zero or more times
*?      Repeats a character zero or more times (non-greedy)
+       Repeats a character one or more times
+?      Repeats a character one or more times (non-greedy)
[aeiou]     Matches a single character in the listed set
[^XYZ]      Matches a single character not in the listed set
[a-z0-9]    The set of characters can include a range
(       Indicates where string extraction is to start
)       Indicates where string extraction is to end
"""

import re
nums = []
file = open('./data/data_90_445833.txt', 'r')
for line in file:
    nums.extend(re.findall('[0-9]+', line))
    print("New line:")
    print(len(nums))
    print(nums) 
file.close()
# print(len(nums))
# print(nums)

the_sum = 0
for num in nums:
    the_sum += int(num)
print(the_sum)





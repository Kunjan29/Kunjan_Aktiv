"""
Write a Python function that accepts a string and counts the number of upper and lower case letters.
"""

string = input("Enter String : ")

def count_upper_lower(string):
count = 0
count1 = 0
for i in string:
	if i.islower():
		count = count + 1
	elif i.isupper():
		count1 = count1 + 1

print("Number of Lowercase Letter in String is : ",count)
print("Number of UpperCase Letter in String is : ",count1)

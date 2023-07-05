"""
 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
"""

lst = [1,2,3,2,2,4,1,2,2]
lst1 = []

def distinct_list(lst):
	for i in lst:
		if i not in lst1:
			lst1.append(i)
	return lst1

result = distinct_list(lst)
print(result)	

"""
Write a Python program to print the even numbers from a given list.
"""

lst = [1,2,3,4,5,8,9,12,13]
lst1 = []

def even_number_list(lst):
	for i in lst:
		if i % 2 == 0:
			lst1.append(i)
	return lst1

result = even_number_list(lst)
print(result)

	
				
	


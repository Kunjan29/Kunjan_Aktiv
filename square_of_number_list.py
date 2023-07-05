"""
Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
"""

def square_of_number():
	lst = list()
	for i in range(1,31):
		lst.append(i**2)
	print(lst)

square_of_number()
		

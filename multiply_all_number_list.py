"""
Write a Python function to multiply all the numbers in a list.

"""

lst = [1,2,3,4,5,6]
def multiply_num(lst):
	mul = 1
	for i in lst:
		mul = mul * i
	return mul

print("Multiplication of all number in list is : ",multiply_num(lst))

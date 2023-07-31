#  Write a Python function to reverses a string if its length is a multiple of 4.

mystr=input("Enter the String :")
if len(mystr) % 4 == 0:
   print(''.join(reversed(mystr)))
else:
	print(mystr)
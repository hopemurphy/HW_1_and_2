# Hope Murphy  created 1/29/17
# Algorithm to convert a decimal (integer) into a binary number using recursion
# Used https://www.programiz.com/python-programming/examples/decimal-binary-recursion 
	#as a good visual representation (picture at top) for what happens in a recursion code
# I also used it as a guide when writing my code and how to properly use 
	#programing topics in the links at the top of the page



dec = int(input("Enter an integer:"))
print("The binary representation is: ")

def convertDecToBin(dec):

	if dec > 0:
		convertDecToBin(dec//2)		
		#This part of the code divides the integer by two to convert it to a base 2 number
		#You have to use integer division in order to get the remainder to print out
		#If the number is less than 1 then the code is finished because 
			#you have completely broken down the number to binary form 
		#If you do dec > -1 then the program will not run 

	print(dec % 2,end = '')
	#This part of the code prints out the remainder of the number in reverse

convertDecToBin(dec)


print("							")
print("The binary representation for comparison (using bin(dec)) is:", bin(dec)[2:])
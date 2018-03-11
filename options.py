#!/usr/bin/env python
n=0
while n!=4:
	print("1.Calculator")
	print("2.Armstrong")
	print("3.Fibonacci")
	print("4.Exit")
	n=int(input("Enter Choice\n"))
	if(n==1):
		# This function adds two numbers 
		def add(x, y):
 		  return x + y

		# This function subtracts two numbers 
		def subtract(x, y):
 			return x - y

		# This function multiplies two numbers
		def multiply(x, y):
  		 return x * y

		# This function divides two numbers
		def divide(x, y):
   			return x / y

		print("Select operation.")
		print("1.Add")
		print("2.Subtract")
		print("3.Multiply")
		print("4.Divide")

		# Take input from the user 
		choice = int(input("Enter choice(1/2/3/4):"))

		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))

		if choice == 1:
   			print(add(num1,num2))

		elif choice == 2:
   			print(subtract(num1,num2))

		elif choice == 3:
  		 print(multiply(num1,num2))

		elif choice == 4:
  		 print(divide(num1,num2))
		else:
   			print("Invalid input")
	elif n==2:
		# initialize sum
		sum = 0
		num=int(input("Enter the number: "))
		# find the sum of the cube of each digit
		temp = num
		while temp > 0:
   			digit = temp % 10
   			sum += digit ** 3
   			temp //= 10

		# display the result
		if num == sum:
   			print("It is an Armstrong number")
		else:
   			print("It is not an Armstrong number")
	elif n==3:
		a=int(input("Enter the first number of the series "))
		b=int(input("Enter the second number of the series "))
		n=int(input("Enter the number of terms needed "))
		print a,b,
		while(n-2):
    			c=a+b
    			a=b
    			b=c
   			print c,
    			n=n-1
		print("")
	elif n==4:
		exit()
	else:
		print("Invalid Input")

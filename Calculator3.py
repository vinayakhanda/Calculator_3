print(" ")

print("Welcome to Calculator 3")
print("      ")
print("Type 1 for addition")
print("Type 2 for subtraction")
print("Type 3 for multyplication")
print("Type 4 for division")
print("")
numque= input("Your Answer : ")


num1= int(input("Enter 1st Number : "))
num2= int(input("Enter 2nd number : "))

if(numque == '1'):
	print("answer is",num1+num2)
elif(numque == '2'):
	print("Answer is",num1-num2)
elif(numque == '3'):
	print("Answer is ",num1*num2)
elif(numque == '4'):
	print("Answer is ",num1/num2)
	
else:
	print("error")
print("")	
print("This calculator was made by Vinayak Handa on 9 may 2021 , Sunday ")
print(" ")
print("Good bye👋")




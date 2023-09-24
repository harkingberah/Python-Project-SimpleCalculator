print("This is a simple calculator that can do addition , multiplication , division and subtraction")
calc_ope = input("What would you like to do. Enter a for addition, s for subtraction , m for multiplication and d for division: ")
num1 = input("What is the first number: ")
num2 = input("What is the second number: ")
num1 = int(num1)
num2 = int(num2)
if calc_ope == "a":
    print( "The answer is ",num1+num2)
elif calc_ope == "s":
     print( "The answer is ",num1-num2)
elif calc_ope == "m":
     print( "The answer is ",num1*num2)
else:
     print( "The answer is ",num1/num2)
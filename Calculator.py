# +CREATE A CALCULATOR!!
#  Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!

value_01 = int(input("Enter first number: "))
value_02 = int(input("Enter second number: "))
operator = input("Which operation you wanna perform: \n a: +    b: -    c: *    d: / :   ")
if(operator == "+"):
    print("The value of ", value_01 , "+" , value_02 , "is: ", value_01 + value_02)
elif(operator == "-"):
    print("The value of ", value_01 , "-" , value_02 , "is: ", value_01 - value_02)
elif(operator == "*"):
    print("The value of ", value_01 , "*" , value_02 , "is: ", value_01 * value_02)
elif(operator == "/"):
    print("The value of ", value_01 , "/" , value_02 , "is: ", value_01 / value_02)
else:
    print("INVALID ENTRY! Please choose from the given options.")
    
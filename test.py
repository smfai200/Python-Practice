import os

num = input("Enter Number: ");
num1 = input("Enter Second Number: ");
choice = input("""\n Chose Your Choice!
    1. ADDITION"
    2. SUBTRACTION"
    3. MULTIPLICATION"
    4. DIVISION
    Enter Your Choice: """);

if (choice == 1):
    print "The Addition is: ", (num+num1)
elif(choice ==2):
    print "The Subtraction is: ", (num-num1)
elif(choice==3):
    print "The Multiplication is: ", (num*num1)
else:
    if(num1 == 0):
        print "The Answer is not Defined Because of Division by Zero!"
    else:
        print "The Division is: ", (num/num1)

print ("\n THANK YOU FOR USING THE CALCULATOR!")




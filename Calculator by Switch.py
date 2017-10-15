
def select(argument,num,num1):
    switch = {
        0: num+num1,
        1: num-num1,
        2: num*num1,
        3: num/num1,
    }
    return switch.get(argument,"WRONG CHOICE!")

check = 0
for check in range(-1,1):
 num = input("Enter Number: ");
 num1 = input("Enter Second Number: ");
 choice = input("""\n Chose Your Choice!
    1. ADDITION"
    2. SUBTRACTION"
    3. MULTIPLICATION"
    4. DIVISION
    Enter Your Choice: """);

 if(choice==1):
        print "The Addition is: ",select((choice-1),num,num1)
        check = 1
 elif(choice==2):
        print "The Subtraction is: ", select((choice-1),num,num1)
        check = 1
 elif(choice ==3):
        print "The Multiplication is: ", select((choice-1),num,num1)
        check = 1
 elif(choice == 4):
        if(num1==0):
            print "DIVISION BY ZERO IS UNDEFINED!"
            check = 0
        else:
            print "The Division is: ", select((choice-1),num,num1)
            check = 1
 else:
        print "Wrong Choice!"
        check = 0



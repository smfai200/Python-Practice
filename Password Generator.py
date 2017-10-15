import random
import string

stringlist = (string.ascii_letters)
digitslist =  (string.digits)
speciallist = ("!@#$%^&*")
check = False

while(not check):
    choice = int(input("Do You want to Generate password\n 1. Yes \n 2. No \n Enter Your Choice: "))
    if(choice == 1):
        strength = int(input("Do you want to Generate \n 1. Weak Password \n 2. Middle-Strength Password"
                         "\n 3. Strong\n Enter Your Choice: "))
        if(strength == 1):
            randompass = "".join(random.sample(stringlist,4)) + "".join(random.sample(digitslist,3))
            check = True
        elif(strength == 2):
            randompass = "".join(random.sample(stringlist,4)) + "".join(random.sample(digitslist,3)) + \
                         "".join(random.sample(speciallist,1))
            check = True
        elif(strength == 3):
            randompass = "".join(random.sample(stringlist, 5)) + "".join(random.sample(digitslist, 4))+ \
                         "".join(random.sample(speciallist, 2))
            check = True
        else:
            print("\n \t Wrong Choice Selected!\n \t Start Again!\n")
            continue
        print("Length of Generated Password is: " + str(len(randompass)))
        print("Generated Password is: " + randompass)

    elif(choice == 2):
        print("Thank you for Using Password Generator")
        check = True
    else:
        print("Wrong Choice!!")




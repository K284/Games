import random
x = random.randint(0,9999)
l = len(str(x))
if l == 1:
    print("It is a single digit number")
elif l == 2:
    print("It is a double digit number")
elif l == 3:
    print("It is a triple digit number")
elif l == 4:
    print("It is a 4-digit number")

c = 1

while True:
    u = int(input("Enter the guessed number: "))
    if x == u:
        print("Yes.  You got it in step",c)
        break
    elif u>x:
        print("Your number is greater than the random number\n")
    elif x > u:
        print("Your number is less than the random number\n")
    c+=1

    

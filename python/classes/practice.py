#1. check if a number is even or odd
#2. A number is positive, negative or 0
#3. Name of week day (1-7) else invalid
#4. a, b, c compare 3 numbers hint: and
# if condition and condition

# a = int(input("enter the value of a :"))
# b = int(input("enter the value of b :"))
# if a > b:
#     print(f"{a}is greater than {b}")
# elif a == b:
#     print(f"{a} is equal t0 {b}")
# else:
#     print(f"{b}is greater than {a}")

# check if no is odd or even
# num = int(input("enter the number :"))
# if num % 2 == 0:
#   print("no is even")
# else:
#   print("no is odd")


# a number is positive, negative or 0
# num = int(input("enter the number :"))
# if num>0:
#   print("the number is positive")
# else :
#   print("the number is negative")


# name of week day(1-7) else invalid

day = int(input("enter the day of week (1-7):"))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
else:
    print("invalid")

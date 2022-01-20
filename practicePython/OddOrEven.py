number = int(input("enter a number"))

check = int(input("enter another number"))

if number % 2 != 0:
    print("number is odd")
elif number % 4 == 0:
    print("number is divisible by 4")
else:
    print("number is even")

message = "Divisible" if number % check == 0 else "not divisible"
print(message)

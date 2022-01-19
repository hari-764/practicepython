age = int(input("enter your age"))
num = int(input("enter the number of times you want the message to be repeated"))

year = 2022

#year_100 = year + (100 - age)


for n in range(num):
    print(f'you will be 100 in {year + (100 - age)}', end="")

import random as r


range_cap = input("input the top range of the number")

if  range_cap.isdigit():
    range_cap = int(range_cap)
    if range_cap < 0:
        print('enter a number greater than 0')
        quit()
else:
    print('Enter a number')
    quit()


random_number = r.randint(0,range_cap)
print(random_number)




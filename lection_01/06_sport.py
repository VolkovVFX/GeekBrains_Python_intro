a = int(input("enter first day km: "))
b = int(input("enter the desired number of km: "))
i = 1

while (a < b):
    a *= 1.1
    i += 1
print(f"on the {i}th day, the athlete achieved a result of at least {b} km.")

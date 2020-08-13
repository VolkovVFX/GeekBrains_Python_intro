n = int(input("enter an integer number: "))
max_number = n%10
n = n//10

while(n>0):
    if n%10>max_number:
        max_number = n%10
    n=n//10

print(max_number)


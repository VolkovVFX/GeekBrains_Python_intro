proceeds = float(input("enter firm proceeds: "))
costs = float(input("enter firm costs: "))

if (proceeds > costs):
    rent = (proceeds - costs) / proceeds * 100
    print("the company works with profit")
    print(f"profitability is {rent:.2f} percent")

    num = int(input("enter the number of employees: "))
    profit_by_emp = rent / num
    print(f"profitability per employee: {profit_by_emp:.2f}")

elif (proceeds == costs):
    print("the company works with zero profit")

else:
    print("the company operates at a loss")

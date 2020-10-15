total=0
for day in range(1,6):
    A = int(input("how many books have you sold on day "+str(day)+"?"))
    total = total + A
    print("total is ", total)
print("The number of books that we sold today is")
print(total)

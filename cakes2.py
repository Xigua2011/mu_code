total = 0
print("how many customers are there today?")
c = int(input())
for i in range(1,c+1):
    print("customer",i, "how many cakes do you want")
    cakes = int( input())
    if cakes >12:
        cakes = cakes +1
        print("you get a free cake")
    total = total+cakes
    print("adding", cakes)
print("I will bake",total, "cakes!")

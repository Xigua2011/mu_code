
numbers = [120, 123, 125, 130, 170]
words = ["hello", "goodbye", "good afternoon", "gfhgfh"]
print(len(words))
words.append("salve")
words.append("bonjour")
print(len(words))
#print(words[3])

#print("what times table do you want?")
#ar = int(input())

#for ar in range(1,13):
#    for i in range(1,13):
#        print(ar, "x", i, "=", i*ar)

#for i in range(0,len(words)):
#   print("word",i, words[i])

words.remove("goodbye")

for w in words:
    print(w)



count = 0
total = 0
for n in numbers:
    if(n < 150):
        count = count + 1
        total = total + n

print("Total", total)
print("average", total/count)

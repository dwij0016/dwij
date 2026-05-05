# a = 15
# d = 55
# c = a-d

# print(c)

f = open('poems.txt', 'r')
d = f.read()
print(d)
f.close()

g = open('greeting.txt' , 'w')
g.write("Hello Good evening")
g.close()


g = open('greeting.txt' , 'a')
g.write("\nHave a nice day")
g.close()

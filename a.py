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

# syxtex = open('folder_name\\file_name' , 'mode of operation(like:- 'r' , 'w' , 'a')')  #folder_name(if any)#
with open('poems.txt' , 'r') as r:
    d = r.read()
with open('new.txt' , 'w') as r:
    d = r.write('hjjhfrsjhfrsdhfd')
with open('new.txt' , 'a') as r:
    d = r.write('\n87758996659')
print(d)

with open('poems.txt' , 'r') as s:
    k = s.read()
print(k)
with open('copy_poems.txt' , 'w') as y:
    g = y.write(k)
print(y)



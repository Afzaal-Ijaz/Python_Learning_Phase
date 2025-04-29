# while loops

idx = 0

while idx <=20:
    print(idx)
    idx +=1

# while loop can also apply on list, tuple and set.

list = ["C", "C++", "Java", "Python", "R"]
index = 0

while index < len(list):
    print(list[index])
    index += 1    

tuple = ("apple","mango","banana","peach","grapes")
i = 0
while i < len(tuple):
    print(tuple[i])
    i +=1

# -For loops

for i in range(4):
    print(i)

for i in range(0, 10, 2):  # start, stop, step
    print(i)

# printing list using for loop

list = ["C", "C++", "Java", "Python", "R"]

for i in list:
    print(i)

# ------FOR WITH BREAK


list = ["C", "C++", "Java", "Python", "R"]
for i in list:
    if i == "Java":
        break
    print(i)


# -----FOR WITH CONTINUE


list = ["C", "C++", "Java", "Python", "R"]
for i in list:
    if i == "Java":
        continue
    print(i)

# the continue will skip the current iteration and move to the next iteration means it will skip the hamzah and move on


# Pass statement


for i in range(10):
    pass           # ---->  it will skip the loop if we dont add pass in the empty loop it will throw an error

print("hello")    
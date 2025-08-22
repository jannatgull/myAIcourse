list = ["Jannat" , "AI full stack" , 2025]
list.reverse()
print("Reverse list:" , list)

n = [1, 2, 3, 4, 5]
square = []
for i in n:
    square.append(i**2)
print("Square of list:" , square)

list = ["Jannat" , "" , "AI fullstack" , 2025]
while "" in list:
    list.remove("")
print(list)

list = ["Jannat" , "AI fullstack" , 2025]
a = list.index("Jannat")
list.insert(a + 2 , "Arfa")
print(list)

list = ["Jannat" , "AI fullstack" , 2025]
if "Jannat" in list:
    a = list.index("Jannat")
    list[a] = "Arfa"
print(list)
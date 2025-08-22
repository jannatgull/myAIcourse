dict = { "a" : 20 , "b" : 30 , "c" : 40}
d = 40
if d in dict.values() :
    print(f"{d} exists in dictionary")
else :
    print(f"{d} does not exists in dictionary")

dict = { "a" : 20 , "b" : 30 , "c" : 40}
min_key = min(dict , key=dict.get)
print("Minimum value:" , min_key)

dict = {"a" : 20 , "b" : 30 , "c" : 40}
keys_to_del = ["b" , "c"]
for i in keys_to_del :
    if i in dict :
        dict.pop(i)
print(dict)

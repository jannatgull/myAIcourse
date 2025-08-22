t = (1, 2, 3, 4, 5)
rev_t = t[: : -1]
print(rev_t)

t = (10, 20, 30 ,40)
value = t[1]
print(value)

t1 = (1,2,3)
t2 = (5,6,7)

t1 , t2 = t2 , t1
print("t1:" , t1)
print("t2:" , t2)
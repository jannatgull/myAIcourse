print("Marks out of 100:")
s1 = int(input("s1:"))
s2 = int(input("s2:"))
s3 = int(input("s3:"))
s4 = int(input("s4:"))
s5 = int(input("s5:"))

totalmarks = 5*100
print("Total marks:" , totalmarks)
obtainedmarks = s1+s2+s3+s4+s5
print("Obtained marks:" , obtainedmarks)
print("Percentage:" , (obtainedmarks / totalmarks) * 100)
print("Average:" , obtainedmarks / 5)
CP = int(input("Enter cost price:"))
SP = int(input("Enter selling price:"))


if SP > CP:
    print("Profit and amount")

elif SP < CP:
    print("Loss and amount")

else:
    print("No profit no loss")
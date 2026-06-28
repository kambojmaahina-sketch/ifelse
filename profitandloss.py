'''enter sale and cost price of a product and cal profit and loss'''
a=int(input("enter sale price:"))
b=int(input("enter cost price:"))
profit=0
loss=0
if a>b:
    profit=a-b
    print(f"profit=",profit)
else:
    loss=b-a
    print(f"loss=",loss)
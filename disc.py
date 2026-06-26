''' Decision control instruction : As we know a problem cant be solved without a decision so to take
decision in python we use if else satatement.
syntax: 
if condition : 
     statement 1
     statement 2
else:
     statement 3
     statement 4
     '''
mrp=float(input("enter mrp of book:"))
disc=0
net=0
if mrp>=500:
   disc=mrp*10/100
else:
   disc=mrp*5/100
net=mrp-disc
print(f"('mrp=',{mrp})")
print(f"('disc=',{disc})")
print(f"('net price=',{net})")

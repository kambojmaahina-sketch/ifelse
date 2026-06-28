'''enter marks of 5 subjects,total and percentage print pass or fail'''
n1=int(input("enter 1st num"))
n2=int(input("enter 2nd num"))
n3=int(input("enter 3rd num"))
n4=int(input("enter 4th num"))
n5=int(input("enter 5th num"))
total=n1+n2+n3+n4+n5
percentage=total/5
print(f"total=",total)
print(f"percentage=",percentage)

if percentage>=40:
   print(f"Result: Pass")
else:
   print(f"Result: Fail")
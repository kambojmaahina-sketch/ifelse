'''enterbasic salary of employee and cal net salary 
..if basic salary <10000 HRA=10%,DA=90%
if basic salary >10000 HRA=20%,DA=95%
'''
a=float(input("enter basic salary:"))
if a <=10000:
   HRA=a*10/100
   DA=a*90/100
else:
   HRA=a*20/100
   DA=a*95/100
net_salary=a+HRA+DA
print(f"basic_salary=",a)
print(f"HRA=",HRA)
print(f"DA=",DA)
print(f"net_salary=",net_salary)
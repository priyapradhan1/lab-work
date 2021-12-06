a=int(input("enter the students in first class"))
b=int(input("enter the students in second class"))
c=int(input("enter the students in third class"))
sum=a//2+b//2+c//2+a%2+b%2+c%2
print(f"total number of desks we need:{sum}")
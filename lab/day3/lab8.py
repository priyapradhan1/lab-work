#  Given a n-digit number. Find the sum of its digits.
num=int(input("enter a number"))
total=0
while num>0:
    digits=num%10
    total=total+digits
    num=num//10
print("the sum of digits of the number entered is",total)
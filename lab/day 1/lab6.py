sum = 0
count = 0
for num in range(1,21):
    if num % 2 == 0:
        sum = sum+num
        count=count+1

    if count == 10:
        break

print("The sum of first 10 even numbers is",sum)

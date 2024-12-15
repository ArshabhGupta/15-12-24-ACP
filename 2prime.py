num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if num % i == 0:
       if i > 9:
           print(i)
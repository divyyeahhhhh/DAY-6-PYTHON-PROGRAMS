n = int(input("Enter a number"))
sum = 0
 
for i in range(1, n):
    if n%i == 0:
        sum += i

if n == sum:
    print(f"{n} is a Perfect number")
else:
    print(f"{n} is not a Perfect number");

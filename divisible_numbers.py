x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

count = 0

for i in range(x, y + 1):
    if i % x == 0:
        print(i, end=" ")
        count += 1

print("\nTotal numbers divisible by x:", count)

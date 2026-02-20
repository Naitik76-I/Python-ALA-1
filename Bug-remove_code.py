print("Number Analysis Program")

total = 0
count = 0
even = 0
odd = 0

n = int(input("Enter how many numbers: "))
i = 0

while i < n:
    num = int(input("Enter number: "))

    total = total + num
    count = count + 1

    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    if num > 0:
        print("Positive")
    else:
        print("Negative")

    i = i + 1

average = total / count

print("Total:", total)
print("Average:", average)
print("Even:", even)
print("Odd:", odd)

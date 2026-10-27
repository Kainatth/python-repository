print("Hello Kaiinatth")
num = 29

if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")

    n = 10
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
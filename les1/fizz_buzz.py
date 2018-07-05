def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return ""

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1

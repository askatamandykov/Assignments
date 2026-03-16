def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_fibonacci(n: int) -> int:
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])
    return lst[n - 1]

def factorial(n: int) -> int:
    if n == 0:
        return 1
    for i in range (n-1, 0, -1):
        n *= i
    return n

def count_vowels(s: str) -> int:
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

def sum_of_digits(n: int) -> int:
    sum = 0
    for i in range(len(str(n))):
        sum += n%10
        n //= 10
    return sum


# This is Assignment 7, not 8

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

def reverse_string(s: str) -> str:
    return s[::-1]

def sum_of_squares(n: int) -> int:
    sum = 0
    for i in range (1, n+1):
        sum += i**2
    return sum


def collatz_sequence_length(n: int) -> int:
    length = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
            length += 1
        else:
            n = 3*n+1
            length += 1
    return length

def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def count_words(s: str) -> int:
    lst = s.split(' ')
    return len(lst)

def sum_of_multiples(n: int, x: int, y: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            sum += i
    return sum

def gcd(a: int, b: int) -> int:
    minimal = min(a, b)
    for i in range (minimal, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def lcm(a: int, b: int) -> int:
    minimum = min(a, b)
    for i in range(1, max(a,b)+1):
        test = minimum * i
        if test % max(a, b) == 0:
            return test

def count_characters(s: str, c: str) -> int:
    return s.count(c)

def digit_count(n: int) -> int:
    return len(str(n))

def is_power_of_two(n: int) -> bool:
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True

def sum_of_cubes(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum

def is_perfect_square(n: int) -> bool:
    root = n ** 0.5
    return root*root == n

def is_armstrong_number(n: int) -> bool:
    sum = 0
    for i in str(n):
        sum += int(i)**len(str(n))
    return sum == n
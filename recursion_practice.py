def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def sum_upto_n(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum_upto_n(n - 1)

def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

def sum_of_array(arr: list) -> int:
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_of_array(arr[1:])

def main():
    # Factorial
    print("Factorial of 5:", factorial(5))

    # Fibonacci
    print("Fibonacci of 5:", fibonacci(5))

    # Sum up to n
    print("Sum of numbers up to 5:", sum_upto_n(5))

    # Sum of Digits
    print("Sum of digits of 1234:", sum_of_digits(1234))

    # Power
    print("2 to the power of 3:", power(2, 3))

    # Palindrome Check
    print("Is 'racecar' a palindrome?:", is_palindrome("racecar"))
    print("Is 'hello' a palindrome?:", is_palindrome("hello"))

    # GCD
    print("GCD of 48 and 18:", gcd(48, 18))

    # Reverse String
    print("Reverse of 'hello':", reverse_string("hello"))

    # Sum of Array
    print("Sum of array [1, 2, 3, 4, 5]:", sum_of_array([1, 2, 3, 4, 5]))

    # Tower of Hanoi
    print("Tower of Hanoi with 3 disks:")
    tower_of_hanoi(3, 'A', 'C', 'B')

if __name__ == "__main__":
    main()

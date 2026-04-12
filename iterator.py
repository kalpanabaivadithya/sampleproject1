import re
import time
import functools

# ================================================================
# 1. ITERATORS
# ================================================================

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


squares_gen = (x ** 2 for x in range(1, 6))


# ================================================================
# 2. DECORATORS
# ================================================================

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [log] calling '{func.__name__}' with args={args}")
        result = func(*args, **kwargs)
        print(f"  [log] '{func.__name__}' returned {result}")
        return result
    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [time] '{func.__name__}' took {elapsed:.6f}s")
        return result
    return wrapper


def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@logger
@timer
def add(a, b):
    return a + b


@repeat(3)
def greet(name):
    print(f"  Hello, {name}!")


# ================================================================
# 3. CLOSURES
# ================================================================

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply


def make_accumulator():
    total = 0
    def add(value):
        nonlocal total
        total += value
        return total
    return add


def power(exponent):
    return lambda base: base ** exponent


# ================================================================
# 4. REGULAR EXPRESSIONS
# ================================================================

EMAIL_RE = re.compile(r'[\w.]+@[\w.]+\.\w+')
DATE_RE  = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
PHONE_RE = re.compile(r'\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b')


# ================================================================
# MAIN
# ================================================================

def main():

    # 1. Iterators
    print("=== ITERATORS ===")
    print("CountDown from 5:", end=" ")
    for n in CountDown(5):
        print(n, end=" ")
    print()
    print("Fibonacci <50:", list(fibonacci(50)))
    print("Squares 1-5:",   list(squares_gen))

    # 2. Decorators
    print("\n=== DECORATORS ===")
    add(4, 6)
    greet("Alice")

    # 3. Closures
    print("\n=== CLOSURES ===")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"double(9) = {double(9)},  triple(9) = {triple(9)}")

    acc = make_accumulator()
    print(f"acc(5)={acc(5)}, acc(10)={acc(10)}, acc(3)={acc(3)}")

    square = power(2)
    cube   = power(3)
    print(f"square(5)={square(5)},  cube(3)={cube(3)}")

    # 4. Regular Expressions
    print("\n=== REGULAR EXPRESSIONS ===")
    text = "Contact alice@example.com or bob@test.org by 2024-07-20. Call 987-654-3210."

    print(f"Emails : {EMAIL_RE.findall(text)}")

    m = DATE_RE.search(text)
    if m:
        print(f"Date   : {m.groupdict()}")

    print(f"Phones : {PHONE_RE.findall(text)}")

    cleaned = re.sub(r'[\w.]+@[\w.]+\.\w+', '[REDACTED]', text)
    print(f"Redacted: {cleaned}")

    parts = re.split(r'[\s,;|]+', "one,  two ;three|four")
    print(f"Split  : {parts}")


if __name__ == "__main__":
    main()
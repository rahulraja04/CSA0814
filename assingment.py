# ==========================================
# Q1 - DECISIONS WITH MANY BOUNDARIES
# ==========================================

print("\nQ1 - Electricity Subsidy Eligibility")

units = 250
ration = True
age = 85

# Using If-Elif-Else

if units <= 100:
    print("Full Subsidy")
elif 101 <= units <= 200 and ration:
    print("Partial Subsidy")
elif units > 200 and age > 80:
    print("Special Subsidy")
else:
    print("No Subsidy")


# ==========================================
# Q2 - LOOPS THAT COUNT ATTEMPTS
# ==========================================

print("\nQ2 - OTP Verification")

correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry")
        continue

    if otp == correct_otp:
        print("Login Successful")
        break

    attempts += 1
    print("Wrong OTP")

else:
    print("Account Locked for 30 minutes")


# ==========================================
# Q3 - VEHICLE REGISTRATION VALIDATOR
# ==========================================

print("\nQ3 - Vehicle Registration Validator")

def normalise(text):
    text = text.strip().upper()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text


def is_valid(reg):

    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):

    if is_valid(reg):
        return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]

    return "Invalid Number"


for raw in ["tn 09 ab 1234", "KA-01-M-0007",
            "TN9AB1234", "TN 22 1234 AB"]:

    reg = normalise(raw)

    print(raw, "->", reg,
          "Valid" if is_valid(reg) else "INVALID")

    if is_valid(reg):
        print("Receipt:", format_number(reg))


# ==========================================
# Q4 - BUILDING LONG TEXT: + OR JOIN()
# ==========================================

print("\nQ4 - String Building Comparison")

import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]


def build_plus(parts):
    text = ""

    for p in parts:
        text += p + ";"

    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    return "".join(f"{p};" for p in parts)


for func in [build_plus, build_join, build_fstring]:

    times = []

    for i in range(3):

        start = time.perf_counter()
        result = func(items)
        end = time.perf_counter()

        times.append(end - start)

    print(func.__name__)
    print("Average Time:", sum(times) / 3)
    print("Length:", len(result))


# ==========================================
# Q5 - FUNCTIONS, PARAMETERS AND SCOPE
# ==========================================

print("\nQ5 - Functions and Scope")


def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):

    if order is None:
        order = []

    order.append(item)
    return order


print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print(add_item("Tea"))
print(add_item("Vada"))


def calculate(price):

    gst = price * 0.05
    total = price + gst

    return total, gst


total, gst = calculate(100)

print("Total:", total)
print("GST:", gst)


# Local Variable

def local_example():
    x = 10
    print("Local:", x)


# Global Variable

x = 20


def global_example():
    global x
    x = 30


local_example()
global_example()

print("Global:", x)


# Nonlocal Variable

def outer():

    x = 10

    def inner():
        nonlocal x
        x = 50

    inner()

    print("Nonlocal:", x)


outer()


# Three Customer Test

customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print(customer1)
print(customer2)
print(customer3)


# ==========================================
# Q6 - RECURSION AND ITS LIMITS
# ==========================================

print("\nQ6 - Recursion and Its Limits")


# A. Simple Recursive Method

def climb(n):

    if n == 1:
        return 1

    if n == 2:
        return 2

    return climb(n - 1) + climb(n - 2)


n = 5

print("Simple Recursion:")
print("Number of ways:", climb(n))


# B. Recursive Method with Memoisation

def climb_memo(n, memo={}):

    if n in memo:
        return memo[n]

    if n == 1:
        return 1

    if n == 2:
        return 2

    memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)

    return memo[n]


n = 6

print("Memoisation:")
print("Number of ways:", climb_memo(n))


# C. Iterative Method

def climb_iterative(n):

    a, b = 1, 2

    if n == 1:
        return 1

    if n == 2:
        return 2

    for i in range(3, n + 1):
        a, b = b, a + b

    return b


print("Iterative Method:")
print("Number of ways:", climb_iterative(1000))


# Recursion Limit Check

import sys

print("Recursion Limit:", sys.getrecursionlimit())


print("\nALL QUESTIONS COMPLETED")

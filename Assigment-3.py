# ==============================
# ASSIGNMENT - 3
# ==============================


# Q1: LISTS AND SLICING
# Daily Rainfall Records

import random

readings = [random.randint(0, 50) for i in range(365)]

weekly = []

for i in range(0, 365, 7):
    total = sum(readings[i:i+7])
    weekly.append(total)

print("Weekly Rainfall:", weekly)
print("Maximum Rainfall:", max(readings))
print("Minimum Rainfall:", min(readings))

moving_avg = []

for i in range(len(readings)-6):
    avg = sum(readings[i:i+7]) / 7
    moving_avg.append(avg)

print("7-Day Moving Average:", moving_avg[:5])

dry_days = [i+1 for i in range(365) if readings[i] == 0]

print("Dry Days:", dry_days)


# ==============================
# Q2: TUPLES, MUTABILITY AND COPYING
# ==============================

import copy

rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

original = [[1, 2], [3, 4]]

alias = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original:", original)
print("Alias:", alias)
print("Shallow:", shallow)
print("Deep:", deep)


# ==============================
# Q3: DICTIONARIES
# Farmer Helpline Complaint Analysis
# ==============================

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]


result = frequencies(calls, STOP)

print("Word Frequencies:", result)
print("Top 3 Words:", top(result, 3))


# ==============================
# Q4: SETS
# Elective Registration Clash Detection
# ==============================

ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (
    ai_elective | iot_elective
)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))


# ==============================
# Q5: LIST COMPREHENSION
# Cleaning Sensor Readings
# ==============================

readings = [5, 7, 55, 3, -60, 9, 6, 12]

# Using for loop

valid = []

for c in readings:
    if -50 <= c <= 50:
        valid.append(c)


# Convert Celsius to Fahrenheit

fahrenheit = []

for c in valid:
    f = (c * 9/5) + 32
    fahrenheit.append(f)

print("Valid Celsius:", valid)
print("Fahrenheit:", fahrenheit)


# Using list comprehension

cleaned = [c for c in readings if -50 <= c <= 50]

print("Cleaned Readings:", cleaned)


# Using map and filter

result = list(map(
    lambda c: (c * 9/5) + 32,
    filter(lambda c: -50 <= c <= 50, readings)
))

print("Using map and filter:", result)


# Finding alarm minutes

alarms = [
    i+1 for i, c in enumerate(readings)
    if -50 <= c <= 50 and not (2 <= c <= 8)
]

print("Alarm Minutes:", alarms)

# TASK 1: Repair the Design

def calculate_bill(filename):
    total = 0
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    if not line.strip():
                        continue

                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid fields")

                    amount = float(parts[2])

                    total += amount
                    report.append(parts[1] + " " + parts[2])

                except (ValueError, IndexError) as e:
                    rejected.append((line_no, line.strip(), str(e)))

        print("Mess Bill Report")

        for item in report:
            print(item)

        print("Total:", total)
        print("Rejected Lines:", rejected)

    except FileNotFoundError:
        print("File not found")


calculate_bill("mess_oct.txt")


# TASK 2: FROM REQUIREMENT TO FILE-PROCESSING DESIGN
# Assignment contains pseudocode and design steps only.
# No complete Python program is provided for this task.


# TASK 3: DESIGN THE ERROR HANDLING

import os
import tempfile


class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    if parts[2] not in ("P", "A"):
        raise InvalidRecord(
            f"invalid status '{parts[2]}'"
        )

    return tuple(parts)


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    if not line.strip():
                        continue

                    reg, date, status = parse_line(line)

                    if status == "P":
                        present += 1
                    else:
                        absent += 1

                except InvalidRecord as e:
                    errors.append((line_no, str(e)))

        if present == 0 and absent == 0 and not errors:
            print("File is empty")

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"File not found: {path}"
        ) from e

    except PermissionError as e:
        raise PermissionError(
            f"Permission denied: {path}"
        ) from e

    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            e.encoding,
            e.object,
            e.start,
            e.end,
            e.reason
        ) from e

    else:
        print("File processed successfully")

    finally:
        print("Processing completed")

    return present, absent, errors


data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

with tempfile.NamedTemporaryFile(
    "w",
    suffix=".csv",
    delete=False,
    encoding="utf-8"
) as tmp:
    tmp.write(data)
    filename = tmp.name

try:
    print(summarise(filename))
finally:
    os.remove(filename)


# TASK 3: MISUSE EXPERIMENT

try:
    total = 10
    print(totall)

except Exception:
    pass


# TASK 4: FILE AND EXCEPTION FORENSICS

# 4.1 Original Program

def save_returns(books):
    log = open("returns.log", "w")

    for b in books:
        log.write(b)

    log.close()


def process(day_file):
    try:
        books = open(day_file).read().split("\n")
        save_returns(books)

    except FileNotFoundError:
        print("missing")


process("day1.txt")
process("day2.txt")
process("day3.txt")


with open("returns.log", "r") as f:
    print(f.read())


# 4.2 Corrected Program

def save_returns(books):
    with open("returns.log", "a", encoding="utf-8") as log:
        for b in books:
            log.write(b + "\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.read().splitlines()

        save_returns(books)

    except FileNotFoundError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(str(e) + "\n")


process("day1.txt")
process("day2.txt")
process("day3.txt")


# 4.3 Manual File Handling

f = open("returns.log", "a")

try:
    f.write("Book returned\n")

finally:
    f.close()


# TASK 5: THE SAME UTILITY ORGANISED FOUR WAYS

# 5.1 (a) ONE SCRIPT
# File name: attendance.py

def read_file():
    print("Reading attendance files")


def calculate():
    print("Calculating attendance")


def report():
    print("Generating report")


if __name__ == "__main__":
    read_file()
    calculate()
    report()


# 5.1 (b) ONE MODULE IMPORTED BY MAIN SCRIPT

# File 1: attendance.py

def read_file():
    print("Reading files")


def calculate():
    print("Calculating statistics")


def report():
    print("Generating report")


# File 2: main.py

import attendance

attendance.read_file()
attendance.calculate()
attendance.report()


# 5.1 (c) THREE MODULES IN ONE FOLDER

# Folder: attendance_project

# File: reader.py

def read_file():
    print("Reading files")


# File: stats.py

def calculate():
    print("Calculating statistics")


# File: report.py

def generate():
    print("Generating report")


# File: main.py

import reader
import stats
import report

reader.read_file()
stats.calculate()
report.generate()


# 5.1 (d) PACKAGE ORGANISATION

# Folder: attendance

# File: __init__.py
# Leave this file empty.


# File: attendance/reader.py

def read_file():
    print("Reading files")


# File: attendance/stats.py

def percentage(present, total):
    return (present / total) * 100


# File: attendance/report.py

def generate():
    print("Generating report")


# File: main.py

from attendance import reader, stats, report

reader.read_file()

print(stats.percentage(20, 25))

report.generate()


# TASK 6: COLLEGE FEST REGISTRATION DESK

import os


def valid_email(email):
    return (
        "@" in email
        and "." in email.split("@")[-1]
        and " " not in email
    )


def process_files(files):
    master = []
    seen = set()
    errors = []
    events = {}

    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8") as f:

                for line_no, line in enumerate(f, 1):
                    try:
                        parts = line.strip().split(",")

                        if len(parts) != 5:
                            raise ValueError("Damaged record")

                        reg, name, dept, email, event = parts

                        if not valid_email(email):
                            raise ValueError("Invalid email")

                        if reg in seen:
                            raise ValueError("Duplicate registration")

                        seen.add(reg)
                        master.append(line.strip())

                        for e in event.split(";"):
                            e = e.strip()

                            if e:
                                events.setdefault(e, []).append(
                                    line.strip()
                                )

                    except ValueError as e:
                        errors.append(
                            f"{filename}, Line {line_no}: {e}"
                        )

        except FileNotFoundError:
            errors.append(f"{filename}: File missing")

        except PermissionError:
            errors.append(f"{filename}: Permission denied")

    # Master list

    with open("master.txt", "w", encoding="utf-8") as f:
        for student in master:
            f.write(student + "\n")

    # Event-wise files

    for event, students in events.items():
        filename = event.replace(" ", "_") + ".txt"

        with open(filename, "w", encoding="utf-8") as f:
            for student in students:
                f.write(student + "\n")

    # Summary report

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write("Total Registrations: " + str(len(master)) + "\n")
        f.write("Total Events: " + str(len(events)) + "\n")

    # Error log

    with open("error_log.txt", "w", encoding="utf-8") as f:
        for error in errors:
            f.write(error + "\n")

    print("Processing Completed")
    print("Total Students:", len(master))
    print("Total Errors:", len(errors))


files = [
    "department1.txt",
    "department2.txt",
    "department3.txt",
    "department4.txt",
    "department5.txt"
]

process_files(files)

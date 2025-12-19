import random

numbers = [random.sample(range(1, 11), 10)]

with open("Sorting/numbers/10_numbers.txt", "w") as f:
    for number in numbers:
        f.write(f"{str(number)}\n")
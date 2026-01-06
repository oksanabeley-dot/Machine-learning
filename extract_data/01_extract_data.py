import random
import string
import csv
from random import randint
# 1 task
with open ("task_1.txt", "w", encoding="utf-8") as f:
    f.write(str(randint(1, 100)))

# 2 task
with open("task_1.txt", "w", encoding="utf-8") as f:
    for i in range(10_000):
        letters = ''.join(random.choices(string.ascii_letters))
        f.write(letters + "\n")

# 3 task
# from collections import Counter
# with open("task_1.txt", "r", encoding="utf-8") as f:
#     text = f.read()
# uppercase = [ch for ch in text if 'A' <= ch <= 'Z']
# counts = Counter(uppercase)
# for letter in sorted(counts):
#     print(f"{letter}: {counts[letter]}")

# 4 task
# # with open("task_1.txt", "r", encoding="utf-8") as f:
#     for _ in range(10):
#         line = f.readline()
#         print(line)

with open("task_1.txt", encoding="utf-8") as f:
    for line in f.readlines()[:10]:
        print(line)

# # with open("task_1.txt", encoding="utf-8") as f:
#     for _ in range(10):
#         print(next(f))
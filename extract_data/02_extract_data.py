# # Task 1. Read first 3 rows from amazon.csv, display columns \

with open("amazon.csv", "r", encoding="utf-8") as f:
    for i in range(3):
        row = f.readline()
        print(row)
 
# # # Task 2. Calculate image_url and display stats
# image_url_count = 0
# with open("amazon.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row['image']:
#             image_url_count += 1
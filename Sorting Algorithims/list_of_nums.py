import random
import csv

num_list = []
numbers = 100_000

for i in range(100_000):
    num_list.append(random.randint(0,10000))

# print(num_list)

with open(r'Python-Projects\Sorting Algorithims\numbers.csv', 'w', newline='') as file:
    # Step 4: Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerow(num_list) # Use writerows for nested list
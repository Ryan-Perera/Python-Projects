import csv 

def numbers():
    nums = []
    with open(r'Python-Projects\Sorting Algorithims\numbers.csv', 'r') as file:
        return list(csv.reader(file))
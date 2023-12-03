import csv
import random

def get_word(difficulty):
    words = []
    with open("Python-Projects\Hangman\dictionary.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if difficulty == 'EASY':
                if len(row[0]) >= 4 and len(row[0]) <= 5:
                    words.append(row) 
            if difficulty == 'MEDIUM':
                if len(row[0]) >= 4 and len(row[0]) <= 5:
                    words.append(row)  
            if difficulty == 'HARD':
                if len(row[0]) >= 8:
                    words.append(row)   
    
    return random.choice(words) 


    


    
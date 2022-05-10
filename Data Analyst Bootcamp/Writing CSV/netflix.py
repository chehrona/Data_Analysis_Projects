# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")
found = None
# Set path for file
csv_path = os.path.join('../Resources', 'netflix_ratings.csv')

# Open the CSV
with open(csv_path, newline='') as netflix:
    csvreader = csv.reader(netflix, delimiter=",")
    # Loop through looking for the video
    for row in csvreader:
        if video not in row:
            found = False
        elif video in row:
            print(f'{row[0]} is rated {row[1]} with rating of {row[-1]}')
            break
        else:
            print(f'Sorry {video} is not in our list')




# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Specify the file to write to the movie data.


# Set a variable to false to check if we found the video
found = False

# Open the NetFlix CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:

            # Set the variable created in Step 1 to confirm we have found the video
            found = True

            # Open the file using "write" mode. Specify the variable to hold the contents
            with open("video_data.txt", "w") as output_file:
                movie_data = (f'Title: {row[0]}\n'
                              f'Rating Level: {row[1]}\n'
                              f'Rated: {row[-1]}')
                print(movie_data)
                output_file.write(movie_data)
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")

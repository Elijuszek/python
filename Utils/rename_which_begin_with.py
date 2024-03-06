import os
import re

def rename_files(directory):
    # Define a dictionary to map numbers to words
    number_to_word = {
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten'
    }

    # List all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for filename in files:
        # Check if the file is a PNG file and its name starts with a number
        if filename.endswith('.png') and re.match(r'^\d+', filename):
            # Extract the number from the filename
            number = re.match(r'^(\d+)', filename).group(1)
            
            # If the number is in the dictionary, rename the file
            if number in number_to_word:
                new_filename = filename.replace(number, number_to_word[number])
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")

# Specify the directory containing the PNG files
directory = './'

# Call the function to rename the files
rename_files(directory)

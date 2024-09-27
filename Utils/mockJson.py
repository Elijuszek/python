import json
import random
import os
from datetime import datetime, timedelta
from multiprocessing import Pool, cpu_count
import time
import string

# Constants
rooms = ["MeetingRoom", "Kitchen", "Bathroom"]
categories = ["Electronics", "Food", "Other"]
num_entries = 100000  # Increased number of mock entries to generate

# Set to track unique titles
existing_titles = set()

# Function to generate a random unique title
def generate_title():
    while True:
        # Generate a random title of length 8-12 using letters and digits
        title_length = random.randint(8, 12)
        title = ''.join(random.choices(string.ascii_letters + string.digits, k=title_length))
        
        # Check if the title is unique
        if title not in existing_titles:
            existing_titles.add(title)
            return title

# Function to generate a random datetime string
def generate_created_on(start_date):
    days_to_add = random.randint(0, 30)
    created_on_date = start_date + timedelta(days=days_to_add)
    return created_on_date.isoformat()

# Function to generate a batch of entries
def generate_entries(batch_size):
    entries = []
    start_date = datetime.now()
    for _ in range(batch_size):
        title = generate_title()
        name = title.lower()  # Set Name as lowercase title
        room = random.choice(rooms)
        category = random.choice(categories)
        priority = random.randint(1, 10)
        created_on = generate_created_on(start_date)

        entries.append({
            "Title": title,
            "Name": name,
            "Room": room,
            "Category": category,
            "Priority": priority,
            "CreatedOn": created_on
        })
    return entries

# Function to display progress
def display_progress(current, total):
    percent_finished = (current / total) * 100
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generated Entries: {current} \\ {total} | {percent_finished:.2f}% finished")

# Generate mock data with multiprocessing
if __name__ == '__main__':
    start_time = time.time()  # Start timing
    shortages = []

    batch_size = num_entries // cpu_count()  # Divide the workload among available CPU cores

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(generate_entries, [batch_size] * cpu_count())

    # Flatten the list of results and display progress
    for i, batch in enumerate(results):
        shortages.extend(batch)
        display_progress((i + 1) * batch_size, num_entries)

    # Write to JSON file
    with open('shortages.json', 'w') as json_file:
        json.dump(shortages, json_file, indent=2)

    # Final output message
    end_time = time.time()  # End timing
    print("shortages.json generated successfully.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

#!/usr/bin/env python3

import os
import requests

# Define the directory
dir = "/data/feedback/"

# List all text files
files = [f for f in os.listdir(dir) if f.endswith('.txt')]

# Iterate over each file
for file in files:
    with open(dir + file, 'r') as f:
        lines = f.readlines()

        # Extract data from the file
        title = lines[0].strip()
        name = lines[1].strip()
        date = lines[2].strip()
        feedback = lines[3].strip()

        # Build the dictionary
        data = {
            "title": title,
            "name": name,
            "date": date,
            "feedback": feedback,
        }

        # Post the data to the company's website
        response = requests.post("http://<corpweb-external-IP>/feedback", json=data)

        # Check the status of the request
        if response.status_code != 201:
            print("Error: Failed to upload feedback. Status code:", response.status_code)
        else:
            print("Feedback uploaded successfully.")


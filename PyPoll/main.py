# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:17:41 2023

@author: lenal
"""
import os
import csv

# Set the path to the budget data file
election_data = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner =""
winner_votes = 0

# Read the budget data file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
# Loop through each row in the dataset
    for row in csvreader:
        # Update the total number of votes cast
        total_votes += 1
        
        # Get the candidate's name
        candidate = row[2]
        
        # Update the candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    
    # Find the winner of the election based on popular vote
    for candidate, votes in candidates.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
    
# Create a string with the analysis results
report = ""
report += "Election Results\n"
report += "-------------------------\n"
report += f"Total Votes: {total_votes}\n"
report += "-------------------------\n"
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    report += f"{candidate}: {percentage:.3f}% ({votes})\n"
report += "-------------------------\n"
report += f"Winner: {winner}\n"
report += "-------------------------\n"

# output text file into my directory
output_file = os.path.join("analysis", "results.txt")  

with open(output_file, "w") as file:
    file.write(report)
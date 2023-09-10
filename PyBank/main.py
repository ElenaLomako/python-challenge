# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:17:41 2023

@author: lenal
"""
import os
import csv

# Set the path to the budget data file
budget_data = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999]

# Read the budget data file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
# Loop through each row in the dataset
    for i, row in enumerate(csvreader):
        # Update the total number of months
        total_months += 1
        
        # Update the net total amount of "Profit/Losses"
        net_total += int(row[1])
        
        # Calculate the change in profit/loss
        if i > 0:  # Exclude the first row
            change = int(row[1]) - previous_profit
            
            # Add the change to the list of changes
            changes.append(change)
            
            # Check if the current change is the greatest increase or decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
     
        #Update previous profit
        previous_profit=int(row[1])
      
    # Calculate the average change
    average_change = sum(changes) / len(changes)
       
    

# Print the analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
    
# Create the financial analysis report
report = f"Financial Analysis\n" \
         f"----------------------------\n" \
         f"Total Months: {total_months}\n" \
         f"Net Total: ${net_total}\n" \
         f"Average Change: ${round(average_change, 2)}\n" \
         f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" \
         f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"

# output text file into my directory
output_file = os.path.join("analysis", "results.txt")  

with open(output_file, "w") as file:
    file.write(report)
#The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add out dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file
    #for row in file_reader:
       # print(row)

# Assign a variable to save the file to a path
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file. 
#outfile.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Close the file 
#outfile.close()
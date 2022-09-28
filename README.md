# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who recieved votes. 
3. Calculate the total number of votes each candidate has received.
4. Calculate the percentage of vote each candidate has won. 
5. Determine the winner of the election based on popular vote.
6. Get a complete list of the counties. 
7. Calculate the voter turnout for each county.
8. Calculate the percentage of votes from each county out to the total count.
9. Determine the county with the highest turnout. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.71.2

## Results Summary

### Candidate Results
 
- There were 369,711 votes cast in the election. 
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes. 
  - Diana DeGette recieved 73.8% of the vote and 272,892 votes. 
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes. 
- The winner of the election was: 
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 votes. 

### County Results
- The counties were: 
  - Jefferson
  - Denver
  - Arapahoe
- The voter turnout for each county were: 
  - Jefferson county had 10.5% of the votes with 38,855 voters.
  - Denver county had 82.8% of the votes with 306,055 voters.
  - Arapahoe county had 6.7% of the votes with 24,801 voters.
- The county with the highest turnout was: 
  - Denver county, with 82.8% of the votes and 306,055 voters.

## Summary

### Script Versatility

As outlined in the project overview, this script was used to calculate and/or determine nine deliverables. The script was written in a way that these nine deliverables can be determined from any election data. The candidate list and the county list were not hardcoded for this specific data set. Instead, the script was written to build a list of candidates and a list of counties using an if statement to append the list when a new candidate or county name appeared in the data as it searched through each row of data. On top of that, empty dictionaries were also established so that once the code determined the candidates and the counties, it can write the keys (candidate name and county name) and calculate the value for each (votes) to the dictionaries. 

```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}
```

```
  # If the candidate does not match any existing candidate add it to the candidate list
  if candidate_name not in candidate_options:

      # Add the candidate name to the candidate list.
      candidate_options.append(candidate_name)

      # And begin tracking that candidate's voter count.
      candidate_votes[candidate_name] = 0

  # Add a vote to that candidate's count
  candidate_votes[candidate_name] += 1

  # If statement that checks that the
  # county does not match any existing county in the county list.
  if county_name not in county_list:

      # 4b: Add the existing county to the list of counties.
      county_list.append(county_name)

      # 4c: Begin tracking the county's vote count.
      county_votes[county_name] = 0

  # 5: Add a vote to that county's vote count.
  county_votes[county_name] += 1
```

The rest of the code then uses for loops and if statements to search through the dictionaries created to print the results to the output file, election_analysis.txt. 

```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_count):
                    county_count = votes
                    largest_county = county_name
        
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```
    
    
### Script Modifications

This script works for any election results data however, some modifications maybe be necessary. The file_to_load path will need to be updated to the proper csv file with the new data and the path itself may also need to be updated if it is in a different directory. 

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

The script also expects the candidate names to be in column 3 and the county name to be in column 2. Those indexes in the script may need to be updated accordingly if that information is in different columns. 

```
 # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
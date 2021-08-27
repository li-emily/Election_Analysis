# Objectives
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

#empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        #print candidate name from each row
        candidate_name = row[2]

        #add candidate name to candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
            #start counting candidate vote count
            candidate_votes[candidate_name] = 0
        
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#determine vote percentage
for candidate_name in candidate_options:
    #find votes for each candidate
    votes = candidate_votes[candidate_name]
    #set vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    #print percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
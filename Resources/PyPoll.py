# # Open a csv file the Direct Method:
# # Assign a variable for the file to load and the direct path to that file:
# file_to_load = '/Users/eryser/Desktop/analysis_projects/M3_python/Resources/election_results.csv'

# # Open the file as 'read only' by either method below:
# #election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

# # Close the file.
# election_data.close()

# # Indirect Method
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # How to write to a file:
# # Create file path and name:
# file_to_save = 'analysis/election_analysis.txt'

# # Open the file:
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     title = "Counties in the Election\n------------"
#     txt_file.write(title)
#     txt_file.write("\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Define a list of candidates.
candidate_options = []

# Define a dictionary of candidate votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Increase the total vote counter.
        total_votes += 1

        # Print the candidate name from each row at column index position 2.
        candidate_name = row[2]

        # Only if the candidate name is unique:
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate_options list.
            candidate_options.append(candidate_name)
        
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n.")

# Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
# for row in file_reader:
    # print(row)

  



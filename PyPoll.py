#Add our dependencies 

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes=0 

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Read and print the header row. (Why does it print the header when using next?)
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
    
print(total_votes)

    


    



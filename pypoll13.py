import os
import csv

import csv
file_name = "03-Python_Homework_PyPoll_Resources_election_data.csv"
with open(file_name) as myfile:
   csvreader = csv.reader(myfile)
   csvreader = csv.reader(myfile, delimiter=",")
   csv_header = next(csvreader)
   for row in csvreader:
       print(row) 






# Objective 3: Create the lists to store data. Initialize


count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

for row in csvreader:
# Count the total number of votes
        count = count + 1

  # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


# couldnt get this file 







   
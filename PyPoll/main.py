
import os
import csv
import string

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\Resources\election_data.csv')

OverallVotes=[]
DifferentCandidates = []

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    #Count the total number of votes cast.

    for row in csvreader:
        OverallVotes.append(row[2])
        
        if (row[2]) not in DifferentCandidates:
            DifferentCandidates.append(row[2])

# Print the percentage and number of votes each candidate received.
    for eachname in DifferentCandidates:
        print(f"{eachname} received {OverallVotes.count(eachname)} votes.")
        print(f"This represents {100*OverallVotes.count(eachname)/len(OverallVotes)}% of the votes.")

# Print the number of candidates.
print(f"There were a total of {len(DifferentCandidates)} candidates running for office.")

#Print the overall number of votes cast in the election.
print(f"There were a total of {len(OverallVotes)} votes cast in this election.")

occurences={}

for name in OverallVotes:
    if name in occurences.keys():
        occurences[name] += 1
    else:
        occurences[name] = 1

(max(occurences.keys(), key=occurences.get))
print(f"The winner of the election was {max(occurences.keys(), key=occurences.get)}")










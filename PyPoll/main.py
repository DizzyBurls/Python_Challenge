
import os
import csv
import string

WriteFile="C:\\Users\\chris\\Documents\\Data Analytics Bootcamp\\Homework Tasks\\Homework Task 3\\Python_Challenge\\PyPoll\\Analysis\\Election_results.txt"
file=open(WriteFile, "w")

file.write('Election Results:\n')
file.write('-------------------------------------------------------\n')

# Stipulate the location of the CSV file housing the data to be analysed.

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\Resources\election_data.csv')

# Establish lists to populate:

OverallVotes=[]
DifferentCandidates = []

print("Election Results")
print("--------------------------------------------------")

# Read the CSV file:

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Count the total number of votes cast.

    for row in csvreader:
        OverallVotes.append(row[2])
        
        if (row[2]) not in DifferentCandidates:
            DifferentCandidates.append(row[2])

    # Print the overall number of votes cast in the election.

    VotesCast=len(OverallVotes)

    print(f"Total Votes: {VotesCast}")
    file.write('Total Votes Cast: ')
    file.write(str(VotesCast))
    file.write('\n-------------------------------------------------------\n')
    print("--------------------------------------------------")

    # Print the percentage and number of votes each candidate received.

    for eachname in DifferentCandidates:
        
        percentage=100*OverallVotes.count(eachname)/len(OverallVotes)
        RoundedPercentage=round(percentage, 3)

        IndCandidateVotes=OverallVotes.count(eachname)
        print(f"{eachname}: {RoundedPercentage}% ({IndCandidateVotes})")

        file.write(eachname)
        file.write(': ')
        file.write(str(RoundedPercentage))
        file.write('% (')
        file.write(str(IndCandidateVotes))
        file.write(')\n')

# Find the election winner using a dictionary:
occurences={}

# Set up a count:

for name in OverallVotes:
    if name in occurences.keys():
        occurences[name] += 1
    else:
        occurences[name] = 1

#Find the maxmium number of occurences and the corresponding key in the dictionary:

Winner=(max(occurences.keys(), key=occurences.get))

# Print the winner's name.

print("--------------------------------------------------")
print(f"Winner: {Winner}")
print("--------------------------------------------------")

Winner=(max(occurences.keys(), key=occurences.get))

file.write('-------------------------------------------------------\n')
file.write('Winner: ')
file.write(Winner)
file.close()




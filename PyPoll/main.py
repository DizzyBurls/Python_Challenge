
import os
import csv
import string

# Select the location of the output TXT file.

WriteFile="C:\\Users\\chris\\Documents\\Data Analytics Bootcamp\\Homework Tasks\\Homework Task 3\\Python_Challenge\\PyPoll\\Analysis\\Election_Results.txt"
file=open(WriteFile, "w")

file.write('Election Results:\n')
file.write('-------------------------------------------------------\n')

# Stipulate the location of the CSV file which houses the data to be analysed.

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\Resources\election_data.csv')

# Establish lists to populate in future calculations:

OverallVotes=[]
DifferentCandidates = []

print("Election Results")
print("--------------------------------------------------")

# Read the CSV file:

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Create a new list which stores the candidate name for each vote in the election.

    for row in csvreader:
        OverallVotes.append(row[2])
        
        # Create a new list which stores the names of all the candidates ONCE.

        if (row[2]) not in DifferentCandidates:
            DifferentCandidates.append(row[2])

    # Create a variable which calculates the overall number of votes cast in the election.

    VotesCast=len(OverallVotes)

    # Print to both the terminal and the output TXT file.

    print(f"Total Votes: {VotesCast}")
    file.write('Total Votes Cast: ')
    file.write(str(VotesCast))
    file.write('\n-------------------------------------------------------\n')
    print("--------------------------------------------------")

    # Calculate the percentage and number of votes each candidate received.

    for eachname in DifferentCandidates:
        
        IndCandidateVotes=OverallVotes.count(eachname)

        percentage=100*IndCandidateVotes/VotesCast
        RoundedPercentage=round(percentage, 3)

        
        # Print to both the terminal and the output TXT file.

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

# Print the winner's name to the terminal and the output TXT file.

print("--------------------------------------------------")
print(f"Winner: {Winner}")
print("--------------------------------------------------")

file.write('-------------------------------------------------------\n')
file.write('Winner: ')
file.write(Winner)
file.close()




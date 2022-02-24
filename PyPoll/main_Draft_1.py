
import os
import csv
import string

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\Resources\election_data.csv')

VoterID=[]
County=[]
Candidate=[]
OverallVotes=[]
DifferentCandidates = []

#SelectCandidate = input("Whose election performance would you like to see? ")

found = False

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Print the headers that exist in the sources file.

    #print(f"Header: {csv_header}")

    for row in csvreader:
        OverallVotes.append(row[2])
        
        #if (row[2]) == SelectCandidate:
            #print(row[2] + " secured the vote of " + row[0] + " from " + row[1] + ".")
            #found = True
            #Candidate.append(row[2])
            #County.append(row[1])
            #VoterID.append(row[0])

        if (row[2]) not in DifferentCandidates:
            DifferentCandidates.append(row[2])

    
    #if found is False:
        #print("No candidate matches that description.")

#cleaned_election_csv = zip(VoterID, County, Candidate)

#output_path = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\cleaned_election_data.csv')

#with open(output_path, "w", newline='') as csvfile:
    #writer = csv.writer(csvfile)

    #writer.writerow(['Voter_ID', 'County', 'Candidate'])

    #writer.writerows(cleaned_election_csv)

# Print the number of votes each candidate received.
    for eachname in DifferentCandidates:
        print(f"{eachname} received {OverallVotes.count(eachname)} votes.")
        print(f"This represents {100*OverallVotes.count(eachname)/len(OverallVotes)}% of the votes.")

# Print the list of candidate names.
#print(DifferentCandidates)S

# Print the number of candidates.
print(f"There were a total of {len(DifferentCandidates)} candidates running for office.")

#print(f"The candidate you enetered received {len(Candidate)} votes.")

#Print the overall number of votes.
print(f"There were a total of {len(OverallVotes)} votes cast")

    for eachname in DifferentCandidates:
        if len()







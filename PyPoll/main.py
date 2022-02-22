
import os
import csv

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\Resources\election_data.csv')

VoterID=[]
County=[]
Candidate=[]

SelectCandidate = input("Whose election performance would you like to see? ")

found = False

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        if (row[2]) == SelectCandidate:
            print(row[2] + " secured the vote of " + row[0] + " from " + row[1] + ".")
            found = True
            Candidate.append(row[2])
            County.append(row[1])
            VoterID.append(row[0])

if found is False:
        print("No candidate matches that description.")
#print(Candidate)
cleaned_election_csv = zip(VoterID, County, Candidate)

output_path = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyPoll\cleaned_election_data.csv')

with open(output_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Voter_ID', 'County', 'Candidate'])

    writer.writerows(cleaned_election_csv)





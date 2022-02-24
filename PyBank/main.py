
import os
import csv
import string

# WriteFile="C:\\Users\\chris\\Documents\\Data Analytics Bootcamp\\Homework Tasks\\Homework Task 3\\Python_Challenge\\PyBank\\Analysis\\Bank_results.txt"
# file=open(WriteFile, "w")

# file.write('Bank Results:\n')
# file.write('-------------------------------------------------------\n')

# Stipulate the location of the CSV file housing the data to be analysed.

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyBank\Resources\budget_data.csv')

print("Bank Results")
print("--------------------------------------------------")

# Read the CSV file:
MonthList=[]

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Count the total number of months.

    for row in csvreader:
        MonthList.append(row[0])

    NumMonths=len(MonthList)

    print(f"Total Months: {NumMonths}")








    
#file.close()





import os
import csv
import string

WriteFile="C:\\Users\\chris\\Documents\\Data Analytics Bootcamp\\Homework Tasks\\Homework Task 3\\Python_Challenge\\PyBank\\Analysis\\Bank_results.txt"
file=open(WriteFile, "w")

file.write('Bank Results:\n')
file.write('-------------------------------------------------------\n')

# Stipulate the location of the CSV file housing the data to be analysed.

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyBank\Resources\budget_data.csv')

print("Bank Results")
print("--------------------------------------------------")

# Read the CSV file:
MonthList=[]
PandLList=[]
DiffProf=[]


with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Count the total number of months.

    for row in csvreader:
        MonthList.append(row[0])
        PandLList.append(int(row[1]))
    
    NumMonths=len(MonthList)
    print(f"Total Months: {NumMonths}")
    

def sum(numbers):
    Aggregate = 0
    for number in numbers:
        Aggregate += number
    return Aggregate

# Test your function with the following:

TotalPandL=sum(PandLList)
print(f"Total Profit and Loss: ${TotalPandL}") 

# Use a function to create a new list with the CHANGE in profit each month recoreded in it.
def difference (MonthList):
    for i in range(1, len(MonthList)):
        DiffProf.append(MonthList[i] - MonthList[i-1])
        
difference(PandLList)

# Use previously established SUM function to determine the average monthly change in profit.
AverageProf=(sum(DiffProf))/(len(MonthList)-1)
Limited_AverageProf=round(AverageProf, 2)
print(f"Average Change: ${Limited_AverageProf}")

MaxIncrease=DiffProf[0]
iMax=0

for i in range(1, len(MonthList)-1):
        if MaxIncrease<=DiffProf[i]:
            MaxIncrease=DiffProf[i]
            iMax=i
            

print(f"Greatests increase in profits: {MonthList[iMax+1]} (${MaxIncrease})")


MaxDecrease=DiffProf[0]
iMin=0

for i in range(1, len(MonthList)-1):
        if MaxDecrease>=DiffProf[i]:
            MaxDecrease=DiffProf[i]
            iMin=i

print(f"Greatests decrease in profits: {MonthList[iMin+1]} (${MaxDecrease})")

file.close()




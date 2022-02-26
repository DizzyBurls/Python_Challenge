
import os
import csv
import string

# Stipulate the location of the CSV file which houses the data to be analysed.

csvpath = os.path.join(r'C:\Users\chris\Documents\Data Analytics Bootcamp\Homework Tasks\Homework Task 3\Python_Challenge\PyBank\Resources\budget_data.csv')

print("Financial Analysis")
print("--------------------------------------------------")

# Establish some lists for future operations.
 
MonthList=[]
PandLList=[]
DiffProf=[]

# Read the CSV file:

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the headers when reading the source file.
    
    csv_header = next(csvfile)

    # Create a list of all the months in the source file.
    # Creare a list of all the profits in the source file.

    for row in csvreader:
        MonthList.append(row[0])
        PandLList.append(int(row[1]))

    # Determine the number of months.

    NumMonths=len(MonthList)
    print(f"Total Months: {NumMonths}")
    
# Create a function which can add all of the values in a list.

def sum(numbers):
    Aggregate = 0
    for number in numbers:
        Aggregate += number
    return Aggregate

# Run the SUM function on the profit list created earlier:

TotalPandL=sum(PandLList)
print(f"Total: ${TotalPandL}") 

# Create a function which builds a new list with the CHANGE in profit each month recoreded in it.

def difference (MonthList):
    for i in range(1, len(MonthList)):
        DiffProf.append(MonthList[i] - MonthList[i-1])

# Run the DIFFERENCE function on the profit list created earlier.

difference(PandLList)

# Use previously established SUM function to determine the average monthly change in profit.

AverageProf=(sum(DiffProf))/(len(MonthList)-1)

# Round it to 2 decimal places:

Limited_AverageProf=round(AverageProf, 2)
print(f"Average Change: ${Limited_AverageProf}")

# Create variables for Max Profit calculations.

MaxIncrease=DiffProf[0]
iMax=0

# Run a loop to find biggest positive change in Diff Prof list.

for i in range(1, len(MonthList)-1):
        if MaxIncrease<=DiffProf[i]:
            MaxIncrease=DiffProf[i]
            iMax=i
            

print(f"Greatests Increase in Profits: {MonthList[iMax+1]} (${MaxIncrease})")


# Create variables for Min Profit calculations.

MaxDecrease=DiffProf[0]
iMin=0

# Run a loop to find biggest negative change in Diff Prof list.

for i in range(1, len(MonthList)-1):
        if MaxDecrease>=DiffProf[i]:
            MaxDecrease=DiffProf[i]
            iMin=i

print(f"Greatests Decrease in Profits: {MonthList[iMin+1]} (${MaxDecrease})")


# Write results to text file.

WriteFile="C:\\Users\\chris\\Documents\\Data Analytics Bootcamp\\Homework Tasks\\Homework Task 3\\Python_Challenge\\PyBank\\Analysis\\Financial_Analysis.txt"
file=open(WriteFile, "w")

file.write('Financial Analysis:\n')
file.write('-------------------------------------------------------\n')

file.write('Total Months: ')
file.write(str(NumMonths))
file.write('\n')
file.write('Total: $')
file.write(str(TotalPandL))
file.write('\n')
file.write('Average Change: $')
file.write(str(Limited_AverageProf))
file.write('\n')
file.write('Greatest Increase in Profits: ')
file.write(str(MonthList[iMax+1]))
file.write('   ($')
file.write(str(MaxIncrease))
file.write(')')
file.write('\n')
file.write('Greatest Decrease in Profits: ')
file.write(str(MonthList[iMin+1]))
file.write('   ($')
file.write(str(MaxDecrease))
file.write(')')

file.close()




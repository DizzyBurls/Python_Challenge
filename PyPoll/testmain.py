import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('Tiny_Elecetion_Data.csv')

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(Tiny_Elecetion_Data):

    Ballot_ID = int(Tiny_Elecetion_Data[0])
    County = str(Tiny_Elecetion_Data[1])
    Candidate = str(Tiny_Elecetion_Data[2])

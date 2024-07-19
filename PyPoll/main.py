import os 
import csv 

#  
election_data = os.path.join("Resources", "election_data.csv")

# Identify variables
Candidates = []
Vote_Count = []
Vote_Percentage = []
Total_Votes = 0 

# Open CSV
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    for row in csvreader: 
        
        # Add votes by 1
        Total_Votes += 1 

        if row[2] not in Candidates:
            Candidates.append(row[2])
            Index = Candidates.index(row[2])
            Vote_Count.append(1)
        else:
            Index = Candidates.index(row[2])
            Vote_Count[Index] += 1

    # Calculate percentage from vote counts to 3 decimals
    for Votes in Vote_Count:
        Percentage = (Votes/Total_Votes) * 100
        Percentage = "%.3f%%" % Percentage
        Vote_Percentage.append(Percentage)
            
    # Calculate winner
    Winner = max(Vote_Count)
    Index = Vote_Count.index(Winner)
    Candidate_Winner = Candidates[Index] 

# Print
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(Total_Votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f" {Candidates[i]} : {str(Vote_Percentage[i])} {str(Vote_Count[i])}")
print("--------------------------")
print(f"Winner: {Candidate_Winner}")
print("--------------------------")

# Create txt
output_path = os.path.join("Resources", "analysis")

# Open csv
with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile)

    # Write rows
    csvwriter.writerow("Election Results")
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(str(f"Total Votes: {str(Total_Votes)}"))
    csvwriter.writerow(["----------------------------"])
    for i in range(len(Candidates)):
        csvwriter.writerow(f"(Candidates[i]: {str(Vote_Percentage[i]({str(Vote_Count[i])}))}")
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(f"Winner: {Candidate_Winner}")
    csvwriter.writerow(["----------------------------"])

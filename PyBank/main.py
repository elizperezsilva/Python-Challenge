import os 
import csv 

# CSV file path added
budget_data = os.path.join("Resources", "budget_data.csv")

Profits = [] 
Dates = []
Total_Months = 0
Total_Profit = 0
Value = 0 
Change = 0 

# Open the CSV file 
# Read the CSV file
with open(budget_data, newline="") as csvfile:
    cvsreader = csv.reader(csvfile, delimiter = ",")
  
    csv_header = next(cvsreader)

    #Assign results to variable 
    First_Row = next(cvsreader) 
    Total_Months += 1
    Total_Profit += int(First_Row[1])
    Value = int(First_Row[1])
  
    for row in cvsreader: 
      
        Dates.append(row[0])

        # Calculate Change
        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])
      
        # Calculate the Total Number of Months 
        Total_Months = len(Dates)
        Total_Months += 1

        # Calculate Profit
        Total_Profit = Total_Profit + int(row[1]) 

    # Calculate Greatest increase in Profits
    Greatest_Increase = max(Profits) 
    Greatest_Index = Profits.index(Greatest_Increase)
    Greatest_Date = Dates[Greatest_Index]

    # Calculate Greatest decrease in Profits
    Greatest_Decrease = min(Profits)
    Lowest_Index = Profits.index(Greatest_Decrease)
    Lowest_Date = Dates[Lowest_Index]

    # Calculate average Profit Change
    Average_Profit_Change = sum(Profits)/len(Profits)

#Print
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Total_Months)}")
print(f"Total : ${str(Total_Profit)}")
print(f"Average Change: ${str(round(Average_Profit_Change, 2))}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})")

# Write to file
output_path = os.path.join("Resources", "analysis")

# Open the file
with open(output_path, "w") as csvfile:

    # Write code on another csv
    csvwriter = csv.writer(csvfile)

    # Write first row of header on new csv
    csvwriter.writerow(["Financial Analysis"])

    #Write rows
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(str(f"Total Months: {str(Total_Months)}"))
    csvwriter.writerow(str(f"Total: ${str(Total_Profit)}"))
    csvwriter.writerow(str(f"Average Change: ${str(round(Average_Profit_Change))}"))
    csvwriter.writerow(str(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})"))
    csvwriter.writerow(str(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})"))

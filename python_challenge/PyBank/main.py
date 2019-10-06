# Modules
import os
import csv     # for reading csv files

Months = []
Profit_Loss = []
Differences = []
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""
    
data = os.path.join("C:\\Users\\myles\\Desktop\\HomeworkDA\\python-challenge\\PyBank\\HW_Resources_budget_data.csv")
with open(data, newline='') as csvfile:
   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   # Read the header row first (skip this step if there is no header)
    csv_header = next(csvfile)
    # Count total number of months the data encapsulates
    for row in csvreader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))
    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(Months))
    print("Net Total: $", sum(Profit_Loss))
    

    for i in range(1, len(Profit_Loss)):
        
        # Find average change between months
        Differences.append(Profit_Loss[i] - Profit_Loss[i-1])
        
        # Find average of values
        Average_Change = sum(Differences) / len(Differences)
        
        # Determine greatest increase and date
        Greatest_Increase = max(Differences)
        Greatest_Increase_Date = str(Months[Differences.index(max(Differences))])
        
        
        # Determine greatest decrease and date
        Greatest_Decrease = min(Differences)
        Greatest_Decrease_Date = str(Months[Differences.index(min(Differences))])
        
    # Print Statements
    print("Average Change: $", round(Average_Change))  
    print("Greatest Increase: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
    print("Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")
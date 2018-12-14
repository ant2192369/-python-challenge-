import os
import csv

import csv
file_name = "03-Python_Homework_PyBank_Resources_budget_data.csv"
with open(file_name) as myfile:
   csvreader = csv.reader(myfile)
   csvreader = csv.reader(myfile, delimiter=",")
   csv_header = next(csvreader)
   for row in csvreader:
       print(row)

# create list to store data
profit = []
monthly_changes = []
date = []

# Initialize the variables as required.
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# conduct the task
  

# use count to count number of months     

count = count + 1 
# Will need it when collecting the greatest increase and decrease in profits
date.append(row[0]) 
# Append the profit information & calculate the total profit
profit.append(row[1])
total_profit = total_profit + int(row[1])
#Calculate the average change in profits from month to month. Then calulate the average change in profits
final_profit = int(row[1])
monthly_change_profits = final_profit - initial_profit

# store monthly changes in a list

monthly_changes.append(monthly_change_profits)

total_change_profits = total_change_profits + monthly_change_profits
     
initial_profit = final_profit
 #Calculate the average change in profits
average_change_profits = (total_change_profits/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)

increase_date = date[monthly_changes.index(greatest_increase_profits)]
decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

# print statements 
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

  





















      
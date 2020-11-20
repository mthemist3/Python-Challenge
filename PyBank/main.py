import csv
import os


budget_data = os.path.join('Resources', 'budget_data.csv')

#Define Variables
total_months = 0
month_of_change = []
net_change_list = []
total_net = 0

#Open and read the CSV
with open (budget_data) as csvfile:
   csv_reader = csv.reader(csvfile)
   
   #Clean header
   header = next(csv_reader)
   
   #Reading the header as the first row
   first_row = next(csv_reader)

   #Adding 1 to the total amount of months
   #Note: Doesnt matter what column you are counting
   total_months += 1
   total_net += int(first_row[1])
   prev_net = int(first_row[1])
   
   #Create a for loop to figure out the net changes
   for row in csv_reader:
       total_months += 1
       total_net += int(row[1])
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change]
       month_of_change += [row[0]]

#Add the netchanges and divide by the total number of changes to get net monthly average
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Find the highest and lowest figures in net change:
highest_change = max(net_change_list)
lowest_change = min(net_change_list)

#Locate the value of those changes:
highest_month=net_change_list.index(highest_change)
lowest_month=net_change_list.index(lowest_change)

#Assign the months
best_month = month_of_change[highest_month]
worst_month= month_of_change[lowest_month]

output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits:{best_month}(${highest_change})\n"
   f"Greatest Decrease in Profits:{worst_month}(${lowest_change})\n")
# Print the output (Git Bash)
print(output)

#Exporting file
output_pybank = open("outputpybank.txt", "w")
#Writing each result
output_pybank.write("Financial Analysis\n")
output_pybank.write("----------------------------\n")
output_pybank.write(f"Total Months: {total_months}\n")
output_pybank.write(f"Total: ${total_net}\n")
output_pybank.write(f"Average  Change: ${net_monthly_avg:.2f}\n")
output_pybank.write(f"Greatest Increase in Profits:{best_month}(${highest_change})\n")
output_pybank.write(f"Greatest Decrease in Profits:{worst_month}(${lowest_change})\n")
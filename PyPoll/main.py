import csv
import os

election_data = os.path.join('Resources', 'election_data.csv')

#Define Variables
votes=[]
total_votes=0
county=[]
candidates=[]
correy=[]
khan=[]
li=[]
tool=[]
#Open and read file
with open (election_data) as csvfile:
    csv_reader = csv.reader(csvfile)

    csv_header = next(csv_reader)

#Appending Each row
    for row in csv_reader:
            votes.append(int(row[0]))
            county.append(row[1])
            candidates.append(row[2])

#Finding total votes and each vote per candidate
    total_votes=(len(votes))
    # print(total_votes)

    khan_count = (candidates.count("Khan"))
    # print(khan_count)
    correy_count = (candidates.count("Correy"))
    # print(correy_count)
    li_count = (candidates.count("Li"))
    # print(li_count)
    tool_count = (candidates.count("O'Tooley"))
    # print(tool_count)

#Percentages for each candidate
khan_percent = round(((khan_count/total_votes)*100), 2)
correy_percent = round(((correy_count/total_votes)*100), 2)
li_percent = round(((li_count/total_votes)*100), 2)
tool_percent = round(((tool_count/total_votes)*100), 2)
# print(khan_percent)
# print(correy_percent)
# print(li_percent)
# print(tool_percent)

#Finding the winner
if khan_percent> max(correy_percent, li_percent, tool_percent):
    winner = "Khan"
elif correy_percent> max(khan_percent, li_percent, tool_percent):
    winner = "Correy"
elif li_percent> max(khan_percent, correy_percent, tool_percent):
    winner = "Li"
else:
    winner = "O'Tooley"

output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"Khan: {khan_percent}% ({khan_count})\n"
    f"Correy: {correy_percent}% ({correy_count})\n"
    f"Li: {li_percent}% ({li_count})\n"
    f"O'Tooley: {tool_percent}% ({tool_count})\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")
print(output)

#Exporting file
output_pybank = open("outputpypoll.txt", "w")
#Writing each result
output_pybank.write(f"Election Results\n")
output_pybank.write("----------------------------\n")
output_pybank.write(f"Total Votes: {total_votes}\n")
output_pybank.write("----------------------------\n")
output_pybank.write(f"Khan: {khan_percent}% ({khan_count})\n")
output_pybank.write(f"Correy: {correy_percent}% ({correy_count})\n")
output_pybank.write(f"Li: {li_percent}% ({li_count})\n")
output_pybank.write(f"O'Tooley: {tool_percent}% ({tool_count})\n")
output_pybank.write("----------------------------\n")
output_pybank.write(f"O'Tooley: {tool_percent}% ({tool_count})\n")
output_pybank.write("----------------------------\n")
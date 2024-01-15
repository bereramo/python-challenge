import csv
import os

#Decalring the csv file being worked on and where the output is going to be printed.
load_file = os.path.join('Resources', 'budget_data.csv')
write_file = os.path.join('Analysis', 'budget_data.txt')

#Opening the designated file and stating where the code should start.
with open (load_file) as file:
    reader = csv.reader(file)
    header = next(reader)
    first_line = next(reader)

# Stating the variables.
    months = 0
    net = 0
    net_change_list = []
    greatest_profit = ['',0]
    greatest_loss = ['', 0]


    months +=  1
    net += int(first_line[1])
    previous = int(first_line[1])


    for line in reader:
        months += 1
        net += int(line[1])
        net_change = int(line[1]) - previous
        previous = int(line[1])
        net_change_list.append(net_change)



        if net_change > greatest_profit[1]:
            greatest_profit[1] = net_change
            greatest_profit[0] = line[0]


        if net_change < greatest_loss[1]:
            greatest_loss[1] = net_change
            greatest_loss[0] = line[0]

average_profit_loss = sum(net_change_list)/len(net_change_list)

with open(write_file,"w") as file:
    output = (f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${net_change}
Average Change: ${average_profit_loss}
Greatest Increase in Profits: {greatest_profit[0]} (${greatest_profit[1]})
Greatest Decrease in Profits: {greatest_loss[0]} (${greatest_loss[1]})
""")
    
    print(output)
    file.write(output)
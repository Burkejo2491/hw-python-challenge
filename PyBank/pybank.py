import os
import csv

months = 0
net_total = 0

net_changes_list = []

change = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as data_set:
    csvreader = csv.reader(data_set, delimiter = ',')
    csvheader = next(csvreader)
    jan_data = next(csvreader)
    months = months + 1
    net_total = net_total + int(jan_data[1])
    previous_net = int(jan_data[1])
    
    for row in csvreader:
        months = months + 1
        net_total = net_total + int(row[1])
        change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_changes_list = net_changes_list + [change]
average_change = sum(net_changes_list)/ len(net_changes_list)
max_change_increase = max(net_changes_list) 
max_change_decrease = min(net_changes_list)

print("Total Months:" , (months))
print("Total:" , (net_total))
print("Average Change:" , round(average_change, 2))
print("Greatest Increase in Profits:" , (max_change_increase))
print("Greatest Decrease in Profits:" , (max_change_decrease))


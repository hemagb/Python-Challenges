import os
import csv

file_to_output ="Analysis.txt"
date_rows=[]
dict_date_rows={}
Profit=0
Profit_Date=0
decrease=0
def get_TotalNumMonths():
    return len(date_rows)

def Net_Profit_Losses():
    sum=0  
    for i, v in enumerate(date_rows):
        sum +=int(v[1])
    return sum    

    
    

ProfitChange=0
prev_range=0
greatest_increase=0
greatest_decrease=0
greatest_decrease_date=0
greatest_increase_date=0
average_change=[]
with open("budget_data.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        date_rows.append(row)
        ProfitChange = int(row[1]) - prev_range
        prev_range=int(row[1])
        average_change.append(ProfitChange)
        if(ProfitChange > greatest_increase):
            greatest_increase= ProfitChange
            greatest_increase_date=row[0]
        if(ProfitChange < greatest_decrease):
           greatest_decrease = ProfitChange
           greatest_decrease_date=row[0]

        

#Get total num of months
ttl_months = get_TotalNumMonths()
sum_ProfitLoss = Net_Profit_Losses()
# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(ttl_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(sum_ProfitLoss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(average_change)/ttl_months,2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(Profit_Date) + greatest_increase_date + " ($" + str(greatest_increase) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

    print("Total Months: " + str(ttl_months))
    print("Total Revenue: " + "$" + str(sum_ProfitLoss))
    print("Average Change: " + "$" + str(round(sum(average_change)/ttl_months,2)))
    print("Greatest Increase: " + str(Profit_Date) + greatest_increase_date + " ($" + str(greatest_increase) + ")") 
    print("Greatest Decrease: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")


        
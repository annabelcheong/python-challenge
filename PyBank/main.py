#Import os module to allow creation of file paths across operating systems and import csv module
import os
import csv

#Create file path and join
csvpath = os.path.join("Pybank_data.csv")
with open(csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)


######GET TOTAL MONTHS AND TOTAL PROFIT/LOSS##############

#Test on how many lines are in csv file with row data
    line_count=0
    profit_loss=0
    average_change=0

#Store date into new lists, profit_loss data into 2 separate list. 2nd profit_loss data list is offset by 1 row to calculate difference later on.
    date_list1=[]
    test_list1=[]
    test_list2=[]
    
    for row in csv_reader:
        #line count each row to attain total months
        line_count += 1
        
        #Store lists and create 2 test lists for the profit/loss column to compare difference later.
        date_list1.append(row[0])
        test_list1.append(row[1])
        test_list2.append(row[1])

        #set variable to record sum of profit/loss total (column 2)
        profit_loss=profit_loss + int(row[1])

    #Assign variable to store total months from iteratively counting rows
    months=(int(line_count))
    
    print("Financial Analysis \n-------------------------- ")
    print(f"Months: {months}")
    print(f"Total: ${profit_loss}")    

############GET AVERAGE CHANGE################

#Deletes first entry of test_list2 to move remaining entries up 1 index
del test_list2[0]

#Zip the 2 lists to object
y=zip(test_list1,test_list2)

#Create new list to store the difference between each month's profit/loss value
difference=[]

#Attain difference between each month and store into difference list
for test_list1_i,test_list2_i in y:
    difference.append(int(test_list2_i)-int(test_list1_i))
#print(difference)

#TEST: print(sum(difference))
#TEST: print(len(difference))

#Average change equation, and print Average Change
average_change=sum(difference)/len(difference)
print(f"Average Change:${average_change:.2f}")

#######GET MAX, MIN PROFIT VALUES########

newlist1 = list(map(int, test_list1))
#TEST: print(newlist1)

#Find and assign max and min value of the profit and losses.
max_value=max(newlist1)
min_value=min(newlist1)

#Find the index of the max and min value in the list.
max_index=newlist1.index(max(newlist1))
min_index=newlist1.index(min(newlist1))
#TEST: print(max_index)

print(f"Greatest Increase in Profits: {date_list1[max_index]} (${max_value})")
print(f"Greatest Decrease in Profits: {date_list1[min_index]} (${min_value})")

#########CREATE REPORT SUMMARY AND EXPORT RESULT TO TEXT FILE##########

report=open('PyBank_Summary.txt','w')
report.write("Financial Analysis \n-------------------------- \n")
report.write(f"Months: {months} \n")
report.write(f"Total: ${profit_loss} \n")
report.write(f"Average Change:${average_change:.2f} \n")
report.write(f"Greatest Increase in Profits: {date_list1[max_index]} (${max_value}) \n")
report.write(f"Greatest Decrease in Profits: {date_list1[min_index]} (${min_value})")
report.close()
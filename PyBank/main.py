#Import os module to allow creation of file paths across operating systems and import csv module
import os
import csv

#Create file path and join
csvpath = os.path.join("Pybank_data.csv")
with open(csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

 #Test on how many lines are in csv file with row data
    line_count=0
    a=-1
    i=0
    profit_loss=0
    average_change=0

#Store date into new lists, profit_loss data into 2 separate list. 2nd profit_loss data list is offset by 1 row to calculate difference later on.
    date_list1=[]
    test_list1=[]
    test_list2=[]
    
    for row in csv_reader:
        #print(row)
        line_count += 1
        #print(int(line_count))
        date_list1.append(row[0])
        test_list1.append(row[1])
        test_list2.append(row[1])

        #set variable to record sum of column 2
        profit_loss=profit_loss + int(row[1])
        # TEST: print(row)
        # TEST to see if number is accumulating: print(profit_loss)
        # TEST: print(type(profit_loss))
        # TEST: print(type(row[1]))

     

    months=(int(line_count))
    
    print("Financial Analysis \n-------------------------- ")
    print(f"Months: {months}")
    #print(f"Hello, this is the total profit_loss net at {profit_loss}. It should be 38382578.")
    print(f"Total: ${profit_loss}")
    
    

del test_list2[0]
#print(test_list1)
#print(test_list2)
#print(test_list1[0])
#print(test_list2[0])

y=zip(test_list1,test_list2)
#print(y)

difference=[]

for test_list1_i,test_list2_i in y:
    difference.append(int(test_list2_i)-int(test_list1_i))
#print(difference)

#print(sum(difference))
#print(len(difference))

average_change=sum(difference)/len(difference)
print(f"Average Change:${average_change:.2f}")

newlist1 = list(map(int, test_list1))
#print(newlist1)

max_value=max(newlist1)
min_value=min(newlist1)

max_index=newlist1.index(max(newlist1))
min_index=newlist1.index(min(newlist1))
#print(max_index)

print(f"Greatest Increase in Profits: {date_list1[max_index]} (${max_value})")
print(f"Greatest Decrease in Profits: {date_list1[min_index]} (${min_value})")

#Create report summary
report=open('PyBank_Summary.txt','w')
report.write("Financial Analysis \n-------------------------- \n")
report.write(f"Months: {months} \n")
report.write(f"Total: ${profit_loss} \n")
report.write(f"Average Change:${average_change:.2f} \n")
report.write(f"Greatest Increase in Profits: {date_list1[max_index]} (${max_value}) \n")
report.write(f"Greatest Decrease in Profits: {date_list1[min_index]} (${min_value})")
report.close()

#outputlist = list(newlist1)
#print(outputlist)
#print(type(test_list1))
#print(type(test_list1[3]))
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
    
    
        # print(row[0])
        # print(row[1])
        # total=total+row[1]
        # print(total)

    
# def stats(profit_loss_calcs):
#     date = str(profit_loss_calc[0])
#     profit_loss = float(profit_losss_calc[1])

#     print(str(date)) 
#     print(profit_loss)

    

#Total number of months
 #   line_count=0
 #   for row in csv_reader:
 #       print(len(row))
 #       line_count+=1
 #       print(int(line_count))
 #   months=int(line_count)
 #   print(f"Total Months: {months}")

  #     for profit_loss in row:
   #         total=0
    #        total+= profit_loss
     #   print(total)

   # for row in csv_reader:
   #     total_rows=len(row)
   #     print(int(total_rows))

  #  csv_header= next(csv_file)
  #  print(f"Header: {csv_header}")
 
#for column in csv_reader
 #   float(column[1])!0
#print(csv_reader)

 #   for row in csv_reader:
  #      if float(row[1])!=0:
   #         sum(f"profit {row[0]}")

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

#

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
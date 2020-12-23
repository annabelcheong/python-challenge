#Import os module to allow creation of file paths across operating systems and import csv module
import os
import csv
#Create file path and join
csvpath = os.path.join("Pybank_data.csv")
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    
 #Test on how many lines are in csv file with row data
    line_count=0
    for row in csv_reader:
        print(row)
        line_count += 1
        print(int(line_count))
        
#Total number of months
    line_count=0
    for row in csv_reader:
        print(len(row))
        line_count+=1
        print(int(line_count))
    months=int(line_count)
    print(f"Total Months: {months}")

    for row in csv_reader:
        for profit_loss in row:
            total=0
            total+= profit_loss
        print(total)

    for row in csv_reader:
        total_rows=len(row)
        print(int(total_rows))

  #  csv_header= next(csv_file)
  #  print(f"Header: {csv_header}")
 
#for column in csv_reader
 #   float(column[1])!0
#print(csv_reader)

 #   for row in csv_reader:
  #      if float(row[1])!=0:
   #         sum(f"profit {row[0]}")
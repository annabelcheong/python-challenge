#Import os module to allow creation of file paths across operating systems and import csv module
import os
import csv

#Create file path and join
#print(os.path.abspath(os.curdir))
# os.chdir("..")
# print(os.path.abspath(os.curdir))
csvpath = os.path.join("../PyPoll/Resources/PyPoll_data.csv")
#csvpath = os.path.join("/Users/annabelcheong/Documents/Data_Analytics/python-challenge/PyPoll/Resources/PyPoll_data.csv")
with open(csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    line_count=0
    for row in csv_reader:
        line_count+=1

    print(int(line_count))
   
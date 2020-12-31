#Import os module to allow creation of file paths across operating systems and import csv module
import os
import csv

#Create file path and join
#print(os.path.abspath(os.curdir))
# os.chdir("..")
#print(os.path.abspath(os.curdir))
csvpath = os.path.join("Resources/PyPoll_data.csv")
#csvpath = os.path.join("/Users/annabelcheong/Documents/Data_Analytics/python-challenge/PyPoll/Resources/PyPoll_data.csv")
with open(csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

#CSV FILE RAW DATA - 1st Col: Voter ID, 2nd Col: County, 3rd Col: Candidate

#Quick test to determine the number of voters.
    # line_count=0
    # for row in csv_reader:
    #     line_count+=1

    # print(int(line_count))

    #Create and store Voter ID, County, Candidate data into lists
    voter_id_string=[]
    county=[]
    candidate=[]

    for row in csv_reader:
        voter_id_string.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    ####FIND AND PRINT THE NUMBER OF TOTAL VOTERS####
    voter_id = list(map(int, voter_id_string))
    #TEST: print(voter_id)
    total_voters=len(voter_id)
    print("\nElection Results\n\n------------------------")
    print(f"Total Votes: {len(voter_id)}")
    print("------------------------")

    ####CALCULATE AND PRINT THE % AND NUMBER OF VOTES FOR EACH CANDIDATE####

    #Count up total votes and % for Khan 
    khan_count=candidate.count("Khan")
    print(f"Khan: {khan_count/total_voters*100:.3f}% ({khan_count})")
    
    #Count up total votes and % for Correy 
    correy_count=candidate.count("Correy")
    print(f"Correy: {correy_count/total_voters*100:.3f}% ({correy_count})")

    #Count up total votes and % for Li
    li_count=candidate.count("Li")
    print(f"Li: {li_count/total_voters*100:.3f}% ({li_count})")

    #Count up total votes and % for O'Tooley
    otooley_count=candidate.count("O'Tooley")
    print(f"O'Tooley: {otooley_count/total_voters*100:.3f}% ({otooley_count})")

    ####FIND WINNER####
    from collections import Counter
   
    vote_count=Counter(candidate)
    #TEST: print(f"vote count: {vote_count}")
    max_votes=max(vote_count.values())
    #TEST: print(f"max votes: {max_votes}")

    #Search for candidate with max votes and store in list
    First=[i for i in vote_count.keys() if vote_count[i]==max_votes]
    print("------------------------")
    print(f"Winner: {sorted(First)[0]}")
    print("------------------------")

   ####CREATE SUMMARY REPORT AND EXPORT RESULT TO TEXT FILE####

report=open('analysis/PyPoll_Summary.txt','w')
report.write("Election Results\n\n------------------------\n")
report.write(f"Total Votes: {len(voter_id)}\n")
report.write("------------------------\n")
report.write(f"Khan: {khan_count/total_voters*100:.3f}% ({khan_count})\n")
report.write(f"Correy: {correy_count/total_voters*100:.3f}% ({correy_count})\n")
report.write(f"Li: {li_count/total_voters*100:.3f}% ({li_count}\n")
report.write(f"O'Tooley: {otooley_count/total_voters*100:.3f}% ({otooley_count})\n")
report.write("------------------------\n")
report.write(f"Winner: {sorted(First)[0]}\n")
report.write("------------------------")
report.close()
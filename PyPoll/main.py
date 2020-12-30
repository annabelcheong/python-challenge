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

    #Print the number of voters
    voter_id = list(map(int, voter_id_string))
    #print(voter_id)
    total_voters=len(voter_id)
    print("\nElection Results\n\n------------------------")
    print(f"Total Votes:{len(voter_id)}")
    print("------------------------")

    from collections import Counter
    candidate_counter=Counter(candidate)
    print(candidate_counter)
    
    #Find and Print the winning candidate
    common_candidate=candidate_counter.most_common(1)
    print(f"Winner:{common_candidate}")
    
    # for i in candidate_counter.elements():
    # candidate_perc=candidate_counter/total_voters*100
    # print(candidate_perc)
    




   
    # result_set=set(candidate)
    # results={}
    # for i in result_set:
    #     results[i]=candidate.count(i)
    # print(results)
    # print(type(results))



    #TEST:print(voter_id[0])
    # if voter_id_element in voter_id:
    #     if voter_id_element in voter
    #     voter_duplicate=voter_id.count(voter_id_element)

   
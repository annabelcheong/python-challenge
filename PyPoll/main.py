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
    # candidate_counter=Counter(candidate)
    # print(candidate_counter)
    
    # print(Counter(candidate_counter.keys()))
    # print(Counter(candidate_counter.values()))

    #Find and Print the winning candidate
    # common_candidate=candidate_counter.most_common(1)
    # print(f"Winner:{common_candidate}")

    vote_count=Counter(candidate)
    print(f"vote count: {vote_count}")
    max_votes=max(vote_count.values())
    print(f"max votes: {max_votes}")

    #Search for candidate with max votes and store in list
    First=[i for i in vote_count.keys() if vote_count[i]==max_votes]
    print(sorted(First)[0])
    print(vote_count.keys)

    common_candidate=vote_count.most_common(1)
    print(f"Most Common Method:{common_candidate}")
    print(list(i for i in common_candidate.keys()))
    print(common_candidate[0])
   #Search for candidate with max votes and store in list
    First=[i for i in vote_count.keys()]
    #print(sorted(First)[0])
    print(sorted(First))
    print(vote_count.keys())






    #Count up total votes and % for Khan 
    khan_count=candidate.count("Khan")
    print(f"Khan: {khan_count/total_voters*100:.2f}% ({khan_count})")
    
    #Count up total votes and % for Correy 
    correy_count=candidate.count("Correy")
    print(f"Correy: {correy_count/total_voters*100:.2f}% ({correy_count})")

    #Count up total votes and % for Li
    li_count=candidate.count("Li")
    print(f"Li: {li_count/total_voters*100:.2f}% ({li_count})")

    otooley_count=candidate.count("O'Tooley")
    print(f"O'Tooley: {otooley_count/total_voters*100:.2f}% ({otooley_count})")



   
    # result_set=set(candidate)
    # results={}
    # for i in result_set:
    #     results[i]=candidate.count(i)
    # print(results)
    # print(type(results))


   
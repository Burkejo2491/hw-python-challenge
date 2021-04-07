import os
import csv

voter_id = 0
candidates = []

candidates_votes = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
election_data = os.path.join("Resources" , "election_data.csv")

with open(election_data) as data_set:
    csvreader = csv.reader(data_set, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        candidates = row[2]
        if candidates in candidates_votes.keys():
            candidates_votes[candidates] = candidates_votes[candidates] + 1
        else:
            candidates_votes[candidates] = 1


total_votes = sum(candidates_votes.values())
print("Total Votes:" , (total_votes))

percent = []
for i in candidates_votes:
    percent = (float(candidates_votes [i])/total_votes)*100
    print(f"{i} {round(percent,3)}% {candidates_votes [i]}")

for x in candidates_votes.keys():
    if candidates_votes[x] == max(candidates_votes.values()):
        winner = x
print(f"Winner is {winner}")



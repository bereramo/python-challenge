import csv
import os

# File location and the text location of output.
load_file = os.path.join('Resources','election_data.csv' )
write_file = os.path.join('Analysis', 'election_data.txt' )

#Declaration of Variables
total_ballots = 0
charles_votes = 0
diana_votes =  0
ramon_votes =  0

# The csv file that is being worked on.
with open(load_file) as file:
    reader= csv.reader(file, delimiter= ",")
    header = next (reader)
    
# Establishing which row and the names that are to be differentiated.
    for row in reader:
        total_ballots += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            ramon_votes +=1

# Determining the winner by votes and displaying the correct winner
winner = max(charles_votes,diana_votes, ramon_votes)
if winner == charles_votes:
        winner_name="Charles Casper Stockham"
elif winner == diana_votes:
        winner_name = "Diana DeGette"
elif winner == ramon_votes:
        winner_name = "Raymon Anthony Doane"


# Calculation of the percentages for each candidate.
charles_percentage = (charles_votes/ total_ballots)*100
diana_percentage = (diana_votes/ total_ballots)*100
ramon_percentage = (ramon_votes/ total_ballots)*100

# Printing the results into a sepcific format into the txt file.
with open(write_file,"w") as file:
    output = (f"""
Election Results
-------------------------
Total Votes: {total_ballots}
-------------------------
Charles Casper Stockham: {round(charles_percentage)}% ({charles_votes})
Diana DeGette: {round(diana_percentage)}% ({diana_votes})
Raymon Anthony Doane: {round(ramon_percentage)}% ({ramon_votes})
-------------------------
Winner: {winner_name}
-------------------------
""")
    # Printing everything nice and neat.
    print (output)
    file.write (output)



import csv

csvpath = r"C:\Users\User\python_challange\PyPoll\Resources\election_data.csv"

def read_data():
    data = []
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header row
        for row in csvreader:
            data.append(row)
    return data

def analyze_votes(data):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Iterate over each row in the CSV data
    for row in data:
        # Count total number of votes
        total_votes += 1
        # Extract candidate name from the row
        candidate_name = row[2]  # Assuming candidate name is in the third column
        # Update candidate votes count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

    # Determine the winner based on the popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Read data from the CSV file
data = read_data()
# Perform analysis
analyze_votes(data)
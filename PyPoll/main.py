import csv
FILE_PATH = r"C:\Users\User\python_challange\PyPoll\Resources\election_data.csv"
data =[]
def read_data():
    with open(FILE_PATH, newline="") as file:
        csv_reader=csv.reader(file)
        next(csv_reader,None)

        for row in csv_reader:
            data.append(row)
def analyze_votes():
    # Initialize variables
    total_votes = 0
    candidate_votes = {}
    
    # Read data from the CSV file
    with open(FILE_PATH, newline="") as file:
        csv_reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV
        for row in csv_reader:
            # Count total number of votes
            total_votes += 1
            
            # Extract candidate name from the row
            candidate_name = row["Candidate"]
            
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

# Perform analysis
analyze_votes()
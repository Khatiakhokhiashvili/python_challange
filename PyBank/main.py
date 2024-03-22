import csv

FILE_PATH = "PyBank/Resources/budget_data.csv"
data = []

def read_data():
    with open(FILE_PATH, newline="") as file:
        csv_reader=csv.reader(file)
        next(csv_reader,None) #skip header row

        for row in csv_reader:
            data.append(row)
def analyze_data():
    # Initialize variables
    total_months = 0
    net_profit_loss = 0
    prev_profit_loss = 0
    profit_loss_changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    # Read data from the CSV file
    with open(FILE_PATH, newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            # Count total number of months
            total_months += 1

            # Calculate net total amount of profit/losses
            profit_loss = int(row[1])
            net_profit_loss += profit_loss

            # Calculate change in profit/loss
            if total_months > 1:
                change = profit_loss - prev_profit_loss
                profit_loss_changes.append(change)

                # Update greatest increase and decrease
                if change > greatest_increase[1]:
                    greatest_increase = [row[0], change]
                if change < greatest_decrease[1]:
                    greatest_decrease = [row[0], change]

            # Remember profit/loss for next iteration
            prev_profit_loss = profit_loss

    # Calculate the average change in profit/losses
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    # Print the analysis results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Perform analysis
analyze_data()
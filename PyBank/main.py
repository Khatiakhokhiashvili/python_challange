import csv

FILE_PATH = "PyBank/Resources/budget_data.csv"
data = []

def read_data():
    with open(FILE_PATH, newline="") as file:
        csv_reader=csv.reader(file)
        next(csv_reader,None) #skip header row

        for row in csv_reader:
            data.append(row)

read_data()

def total_num_month():
    #calculate total number of month including data set
    return len(data)  

print("Total month",total_num_month()) 

def total_amount():
    #calculate sum
    total = 0
    for i,j in enumerate(data):
        total += int(j[1])
    return total

print(f"Total  $ {total_amount()}" )

def avarage_change():
    #calculate average number
    changes =[]
    for i in range(1,total_num_month()): #calcualte change
        current_val = int(data[i][1])
        previous_val= int(data[i-1][1])

        change=current_val-previous_val
        changes.append(change) 
 
    avg_of_changes = sum(changes)/len(changes) 
    avg_of_changes = round(avg_of_changes, 2)
    
    print("avarage change",avg_of_changes)
avarage_change()
def greatest_increase_in_profits():
    greatest_change = 0
    greatest_change_data =""

    for i in range(1,total_num_month()):
        current_val=int(data[i][1])
        prev_val=int(data[i -1][1])
        change=current_val-prev_val

        if abs(change)>abs(greatest_change):
            greatest_change=change
            greatest_change_data=data[i][0]

    return greatest_change_data, greatest_change
print(f'greatest increase in  Profits, ${greatest_increase_in_profits ()}')

def greatest_decrease_in_profits():
    greatest_change = 0
    greatest_change_date =""

    for i in range(1,total_num_month()):
        current_val=int(data[i][1])
        prev_val=int(data[i -1][1])
        change=current_val-prev_val
        if change<greatest_change:
            greatest_change=change
            greatest_change_date=data[i][0]
    return greatest_change_date, greatest_change
print(f'greatest decrease in  Profits, ${greatest_decrease_in_profits ()}')

            
# def analyze_data():
#     # Initialize variables
#     total_months = 0
#     net_profit_loss = 0
#     prev_profit_loss = 0
#     profit_loss_changes = []
#     greatest_increase = ["", 0]
#     greatest_decrease = ["", 0]

#     # Read data from the CSV file
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip header row

#         for row in csv_reader:
#             # Count total number of months
#             total_months += 1

#             # Calculate net total amount of profit/losses
#             profit_loss = int(row[1])
#             net_profit_loss += profit_loss

#             # Calculate change in profit/loss
#             if total_months > 1:
#                 change = profit_loss - prev_profit_loss
#                 profit_loss_changes.append(change)

#                 # Update greatest increase and decrease
#                 if change > greatest_increase[1]:
#                     greatest_increase = [row[0], change]
#                 if change < greatest_decrease[1]:
#                     greatest_decrease = [row[0], change]

#             # Remember profit/loss for next iteration
#             prev_profit_loss = profit_loss

#     # Calculate the average change in profit/losses
#     average_change = sum(profit_loss_changes) / len(profit_loss_changes)

#     # Print the analysis results
#     print("Financial Analysis")
#     print("----------------------------")
#     print(f"Total Months: {total_months}")
#     print(f"Total: ${net_profit_loss}")
#     print(f"Average Change: ${average_change:.2f}")
#     print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
#     print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# # Perform analysis
# analyze_data()
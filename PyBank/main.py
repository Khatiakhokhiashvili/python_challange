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

            

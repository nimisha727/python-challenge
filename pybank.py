import os
import csv


# joining the path:
pybank_csv_path = os.path.join("resources","budget_data.csv")

# Assigning the file name:
file = pybank_csv_path

print(file)

# Now opening a file
with open(file, "r") as jumbled_data:
    unjumbled_data = csv.reader(jumbled_data, delimiter=",")
    
    # skip header
    next(unjumbled_data, None)

    row_count = 0
    total_amount = 0
    greatest_inc = 0
    greatest_dec = 0
    monthly_difference = 0
    first_row = next(unjumbled_data)
    prev_row = int(first_row[1])
    total_difference = 0

    for row in unjumbled_data:
 
        row_count = row_count + 1
        total_amount = total_amount + int(row[1])

        monthly_difference = int(row[1]) - prev_row
        prev_row = int(row[1])
        total_difference = monthly_difference + total_difference

        if greatest_inc <= int(row[1]):
            greatest_inc = int(row[1])
            greatest_date = row[0]
        if greatest_dec >= int(row[1]): 
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

    
    
    average = round(total_difference/row_count)

print("=======================================")
print("     Financial Analysis                ")
print("========================================")
print("Total months: " + str(row_count))
print("Total amount: $" + str(total_amount))
print("total average difference is" + str(average))
print("Greatest increase in Revenue: " + greatest_date +  " and ($" + str(greatest_inc) +")")
print("Greatest_dec_date in Revenue: " +  greatest_dec_date +  " and ($" + str(greatest_dec) +")")

# creating a new file
new_file = open("Resources/analysis.txt", "w")

new_file.write("=======================================\n")
new_file.write("     Financial Analysis                \n")
new_file.write("========================================\n")
new_file.write("Total months: " + str(row_count) + "\n")
new_file.write("Total amount: $" + str(total_amount) + "\n")
new_file.write("total average difference is " + str(average) + "\n")
new_file.write("Greatest increase in Revenue: " + greatest_date +  " and ($" + str(greatest_inc) +")\n")
new_file.write("Greatest_dec_date in Revenue: " +  greatest_dec_date +  " and ($" + str(greatest_dec) +")\n")
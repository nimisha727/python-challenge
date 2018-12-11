import os
import csv


# joining the path:
pypoll_csv_path = os.path.join("resources","election_data.csv")

# Assigning the file name:
file = pypoll_csv_path

    

winner_count = 0

# Now opening a file
with open(file, "r") as jumbled_data:
    unjumbled_data = csv.reader(jumbled_data, delimiter=",")
    
    row_count = 0
    candidates = {}
    candidates_percent ={}
    
    # skip header
    next(unjumbled_data, None)

    for row in unjumbled_data:
        row_count = row_count + 1
    
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    for key, value in candidates.items():
        candidates_percent[key] = round((value/row_count) * 100, 2)
    
    #for key in candidates.key():
    #    if candidates[key] > winner_count:
    #        winner = key
    #        winner_count = candidates[key]

    print(" ++++++++++++++++++++++++++++++++++")
    print("|        Voting Analysis            |")
    print(" ++++++++++++++++++++++++++++++++++")
    print("Total Votes: " + str(row_count))
    print(" ++++++++++++++++++++++++++++++++++")
    for key, value in candidates.items():
        print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")\n")
    print(" ++++++++++++++++++++++++++++++++++")
    print("Winner: ")
    print(" ++++++++++++++++++++++++++++++++++")

    # creating a new file
    new_file = open("Resources/voting_analysis.txt", "w")

    new_file.write(" ++++++++++++++++++++++++++++++++++\n")
    new_file.write("|        Voting Analysis            |\n")
    new_file.write(" ++++++++++++++++++++++++++++++++++\n")
    new_file.write("Total Votes: " + str(row_count) +"\n")
    new_file.write(" ++++++++++++++++++++++++++++++++++\n")
    for key, value in candidates.items():
        new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")\n")
    new_file.write(" ++++++++++++++++++++++++++++++++++\n")
    new_file.write("Winner: \n")
    new_file.write(" ++++++++++++++++++++++++++++++++++\n")    




# with open(file, "r") as text:
 #    print(text)

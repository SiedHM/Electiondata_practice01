#Three methods of data reading
#Method1. reading  data
file_to_load='Resources\election_results.csv'
election_data=open(file_to_load,'r')
 #data analyis
election_data.close()
#Method 2. Reading file
file_to_load='Resources\election_results.csv'
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
#Method 3. reading data
import csv
import os
file_to_load= os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
#writing practice
#Method-1
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

#Method-2
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     txt_file.write("Counties in election\n---------------------\nArapahoe\nDenver\nJefferson")
     


#2. We need to have a complte list of the names of all the candidates.
#3. The percentage of vote  each candidate won.
#4.  the total votes for each candidate won.
#5. The winner of the election based on popular vaote

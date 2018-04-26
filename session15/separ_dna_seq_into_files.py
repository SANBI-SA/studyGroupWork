######################################################################################################
# Binning DNA sequences
# Write a program which creates nine new folders – one for sequences between 100 and 199 bases long, 
# one for sequences between 200 and 299 bases long, etc. 
# Write out each DNA sequence in the input files to a separate file in the appropriate folder.
######################################################################################################

import os
import os.path

## create one folder per bin
# for bin_lower in range(100, 1000, 100):  # creates bins that go from  100 - 1000, in increments of 100. These are the start no's
# 	bin_upper = bin_lower + 99  # the upper limit will just be the bin + 99, so the first bin would be 100 - 199
# 	bin_folder_name = str(bin_lower) + "_" + str(bin_upper) # name of folder would be each bin (eg. 100_199)
# 	os.mkdir(bin_folder_name) #create a bunch of directories all in one go

# create a variable to hold the sequence number
seq_number = 1

# process all files that end in .dna
for file_name in os.listdir("."): #returns a list of files and folders. It takes a single argument which is a string containing the path of the folder whose contents you want to search. To get a list of the contents of the current working directory, 
#use the string "." for the path
	#print (file_name)
	if file_name.endswith(".dna"):
		dna_file = open(file_name)
		
# for each line, calculate the sequence length
		for line in dna_file:
			dna = line.strip()
			#print (dna)
			length = len(dna)
			print ("sequence length is " + str(length))

			for bin_lower in range(100, 1000, 100):  # creates bins that go from  100 - 1000, in increments of 100. These are the start num	
				bin_upper = bin_lower + 99
				if length >= bin_lower and length < bin_upper: #cannot be = to upper_bin, because upper bin, starts new directory
					print ("bin is " + str(bin_lower) + " to " + str(bin_upper)) # once we know the correct bin, write out the sequence
					bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
					if not os.path.exists(output_path):
						os.mkdir(output_path)
					output_path = bin_folder_name + "/" + str(seq_number) + ".dna"
					output = open(output_path, "w")
					output.write(dna + '\n')
					output.close()
					seq_number = seq_number + 1
					break
				
		
			


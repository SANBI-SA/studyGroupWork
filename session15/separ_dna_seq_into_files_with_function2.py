######################################################################################################
# Binning DNA sequences
# Write a program which creates nine new folders – one for sequences between 100 and 199 bases long, 
# one for sequences between 200 and 299 bases long, etc. 
# Write out each DNA sequence in the input files to a separate file in the appropriate folder.
######################################################################################################

import os
import os.path

def find_bin(seqlength):
  # we can predict the bin by looking at the number in the hundreds column of sequence length
  # so e.g. 763 -> bin 700_799, 243 -> bin 200_299
  # this number can be extracted by doing an integer division (the // operator) by 100
  bin_number = seqlength // 100 
  if bin_number < 1 or bin_number > 9:
    raise ValueError("No appropriate bin was found for sequence of length {}".format(seqlength))

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

      bin_folder_name = find_bin(length)
      print ("bin is", bin_folder_name) # once we know the correct bin, write out the sequence
      if not os.path.exists(bin_folder_name):
        os.mkdir(bin_folder_name)
      output_path = bin_folder_name + "/" + str(seq_number) + ".dna"
      output = open(output_path, "w")
      output.write(dna + '\n')
      output.close()
      seq_number = seq_number + 1
      break
				
		
			

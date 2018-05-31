#!/usr/bin/python3

###########################################################################################
# Description of script:

# want to slice out the gene coordinate from the vcf list,
# find out if that gene coordinate lies within an operon
# output this information to individual files with the vcf file name
##########################################################################################

import os
import sys
import glob

################################################
# locate all the necessary files and open them
################################################

path_operon_file = "/home/tracey/Desktop/PhD_Project_test_dataset/Broad_and_Public_data/broad_data/KZN_DR/krith_MDR_vcfs/few_vcf_files/shortened_vcfs/*.txt"
operon_files = glob.glob(path_operon_file)
path_variant_files = "/home/tracey/Desktop/PhD_Project_test_dataset/Broad_and_Public_data/broad_data/KZN_DR/krith_MDR_vcfs/few_vcf_files/shortened_vcfs/TKK*"
variant_files = glob.glob(path_variant_files) #list all the files within the above directory

#######################################################################################################################################################################################################################################################################################
# Put the vcf file data into list of lists
# Format of vcf_file:
# CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	G31877:Mycobacterium_tuberculosis_TKK_02_0007
# MT_H37RV_BRD_V5	1	.	T	.	0	LowCov	DP=0;TD=14;BQ=0;MQ=0;QD=0;BC=0,0,0,0;QP=0,0,0,0;PC=2;IC=0;DC=0;XC=0;AC=0;AF=0.00	GT	0/0	CDS,RVBD_0001,RVBD_0001.1,chromosomal replication initiator protein DnaA,trans_orient:+,loc_in_cds:1,codon_pos:1,codon:TTG
########################################################################################################################################################################################################################################################################################

#create empty lists for all the lists I will use
#creating them outside the loop also makes them available outside the loop
operon_data, gene_list, vcf_list = [], [], []
for files in variant_files:
	file_name = files.split('/')[11] # split the path name by forward slash and store the position containing the file name
	#print (file_name)
	open_files = open(files)
	for lines in open_files:
		if not lines.startswith("#"):
			#print (lines)
			line = lines.strip().split('\t') # strip the spaces at both ends of the line
			# and split the line by the tab character,to create a list of lines
			if line[6] == "LowCov" or line[6] == "Amb" or line[6] == "Del;LowCov" or line[6] == "Del;Amb;LowCov": # do not append any line where the coverage depth is low
				continue
			else:
				vcf_list.append(line)
#print (vcf_list[1], file_name)

###########################################################################################################################
# Put the operon data into list of lists
# Format operon data:
# Operon	Start	Stop	Length	Orientation	Average operon coverage	Number of genes in operon	Genes in operon
# MT0001	1	1524	1523	+	69.2	1	MT0001
############################################################################################################################

	for file_names in operon_files:
		open_operon_file = open(file_names)
		for operon_line in open_operon_file:
			operon_lines = operon_line.strip().split('\t')
			if not operon_lines[0].startswith("Operon"):
				operon_data.append(operon_lines)
		#print(operon_data)
	output_file_name = "operon_" + file_name
	for column in vcf_list:
		mut_position = int(column[1])
		for data in operon_data:
			operon_bin_start = int(data[1])
			operon_bin_end = int(data[2])
			#if not data[6:]:
				#continue # the columns with no data, are also unexpressed operons, so they can be skipped)
			#else:
			if (mut_position >= operon_bin_start and mut_position <= operon_bin_end) or (mut_position == operon_bin_start) or (mut_position == operon_bin_end):
				#print(mut_position, operon_bin_start, operon_bin_end, file_name)
				#print(column[0:3], data[0:3], file_name)

				out_line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (file_name, column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8],column[10],data[0],data[1],data[2],data[3],data[4],data[5],data[6:])
				#out_line = file_name + '\t' + str(mut_position) + '\t' + column[2] + '\t' + column[3] + '\t' + column[4]  + '\t' + column[5] + '\t' +  column[6] + '\t' +  column[7] + '\t' +  data[0]  #+ '\t' +  operon_bin_start + '\t' + operon_bin_end # column[8] + '\t' + column[10] + '\t' +  data[0] + '\t' +  str(data[1]) + '\t' +  str(data[2]) + '\t' +  data[3] + '\t' +  data[4] + '\t' +  data[5] + '\t' +  data[6:] + '\t' +  file_name
				print (out_line)

				# with open(output_file_name, "w") as outfile:
				#
				# 	outfile.write(out_line)
				 	#outfile.write("%s\t%s\t%s\t" %(column[1], data[1], data[2]))

		# print (output_file_name)

#!/usr/bin/python3

###########################################################################################
# Description of script:

# want to slice out the gene coordinate from the vcf list,
# find out if that gene coordinate lies within an operon
# output this information to individual files with the vcf file name
##########################################################################################

import os
import os.path
import sys
import glob
# intervaltree from https://pypi.org/project/intervaltree/
# installed into Anaconda using: conda install intervaltree
import intervaltree
################################################
# locate all the necessary files and open them
################################################

path_operon_file = "../data/vcf_operon_overlap/*.txt"
operon_files = glob.glob(path_operon_file)
path_variant_files = "../data/vcf_operon_overlap/TKK*"
variant_files = glob.glob(path_variant_files)  # list all the files within the above directory

#######################################################################################################################################################################################################################################################################################
# Put the vcf file data into list of lists
# Format of vcf_file:
# CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	G31877:Mycobacterium_tuberculosis_TKK_02_0007
# MT_H37RV_BRD_V5	1	.	T	.	0	LowCov	DP=0;TD=14;BQ=0;MQ=0;QD=0;BC=0,0,0,0;QP=0,0,0,0;PC=2;IC=0;DC=0;XC=0;AC=0;AF=0.00	GT	0/0	CDS,RVBD_0001,RVBD_0001.1,chromosomal replication initiator protein DnaA,trans_orient:+,loc_in_cds:1,codon_pos:1,codon:TTG
########################################################################################################################################################################################################################################################################################

# create empty lists for all the lists I will use
# creating them outside the loop also makes them available outside the loop
vcf_list = []
# read in operon data
operon_tree = intervaltree.IntervalTree()
for file_names in operon_files:
    open_operon_file = open(file_names)
    next(open_operon_file)  # skip header line
    for operon_line in open_operon_file:
        operon_fields = operon_line.strip().split('\t')
        operon_bin_start = int(operon_fields[1])
        operon_bin_end = int(operon_fields[2])
        # insert some data into the interval tree at this position
        operon_tree[operon_bin_start:operon_bin_end] = operon_fields
        # operon_data.append(operon_fields)
        # print(operon_data)

for path in variant_files:
    file_name = os.path.basename(path)
    print (file_name)
    input_file = open(path)
    for line in input_file:
        if not line.startswith("#"):
            # print (lines)
            record = line.strip().split('\t')  # strip the spaces at both ends of the line
            # and split the line by the tab character,to create a list of lines
            if "LowCov" in record[6] or "Amb" in record[6]:  # do not append any line where the coverage depth is low
                continue
            else:
                vcf_list.append(record)

###########################################################################################################################
# Put the operon data into list of lists
# Format operon data:
# Operon	Start	Stop	Length	Orientation	Average operon coverage	Number of genes in operon	Genes in operon
# MT0001	1	1524	1523	+	69.2	1	MT0001
############################################################################################################################

    output_file_name = "operon_" + file_name
    out_file = open(output_file_name, "w")
    for record in vcf_list:
        mut_position = int(record[1])
        # return is a set of Interval objects that overlaps this position
        # each Interval object has members start, end, data: data is the thing
        #   you insert when creating the interval tree
        operon_list = operon_tree[mut_position:mut_position + 1]  # must make at least width 1 for search
        # some notes on VCF positions and "size": https://pyvcf.readthedocs.io/en/latest/API.html#vcf-model-record
        assert len(operon_list) < 2, "position {} overlapped with multiple operons: {}".format(mut_position, operon_list)
        if len(operon_list) > 0:
                output_record = [file_name, record[1]]
                output_record.extend(record[3:])
                # turn the set into a list, take the first element,
                # and take its .data attribute
                output_record.extend(list(operon_list)[0].data)
                out_line = "\t".join(output_record) + "\n"
                out_file.write(out_line)
    out_file.close()

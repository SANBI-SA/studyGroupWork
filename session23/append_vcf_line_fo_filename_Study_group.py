#!/usr/bin/python3

###########################################################################################
# Description of script:

# want to slice out the gene coordinate from the vcf list,
# find out if that gene coordinate lies within an operon
# output this information to individual files with the vcf file name
##########################################################################################

import argparse
import os
import os.path
import sys
import glob

def annotate_vcf_with_operon(operon_path, variant_path):
    operon_files = glob.glob(operon_path)
    variant_files = glob.glob(variant_path) #list all the files within the above directory
    #######################################################################################################################################################################################################################################################################################
    # Put the vcf file data into list of lists
    # Format of vcf_file:
    # CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	G31877:Mycobacterium_tuberculosis_TKK_02_0007
    # MT_H37RV_BRD_V5	1	.	T	.	0	LowCov	DP=0;TD=14;BQ=0;MQ=0;QD=0;BC=0,0,0,0;QP=0,0,0,0;PC=2;IC=0;DC=0;XC=0;AC=0;AF=0.00	GT	0/0	CDS,RVBD_0001,RVBD_0001.1,chromosomal replication initiator protein DnaA,trans_orient:+,loc_in_cds:1,codon_pos:1,codon:TTG
    ########################################################################################################################################################################################################################################################################################

    # create empty lists for all the lists I will use
    # creating them outside the loop also makes them available outside the loop
    operon_data, vcf_list = [], []
    # read in operon data
    for file_names in operon_files:
        open_operon_file = open(file_names)
        next(open_operon_file)  # skip header line
        for operon_line in open_operon_file:
            operon_fields = operon_line.strip().split('\t')
            operon_data.append(operon_fields)
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
            for data in operon_data:
                operon_bin_start = int(data[1])
                operon_bin_end = int(data[2])
                if (mut_position >= operon_bin_start and mut_position <= operon_bin_end) or (mut_position == operon_bin_start) or (mut_position == operon_bin_end):
                    # print(mut_position, operon_bin_start, operon_bin_end, file_name)
                    # print(column[0:3], data[0:3], file_name)

                    output_record = [file_name, record[1]]
                    output_record.extend(record[3:])
                    output_record.extend(data)
                    out_line = "\t".join(output_record) + "\n"
                    out_file.write(out_line)
        out_file.close()

################################################
# locate all the necessary files and open them
################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Annotate VCF file with operon names')
    parser.add_argument('operon_path', nargs='?',
                        help='Global specifying path to operon files',
                        default="../data/vcf_operon_overlap/*.txt")
    parser.add_argument('vcf_path', nargs='?',
                        help='Glob pattern with path to VCF files',
                        default="../data/vcf_operon_overlap/TKK*")
    args = parser.parse_args()

    annotate_vcf_with_operon(args.operon_path, args.vcf_path)

############################################################################################
# import the necessary libraries

%pylab inline						# inline lets you plot figures inline, instead of in a new window or shell
import numpy as np					# provides a high-performance multidimensional array and basic tools to compute with and manipulate 									these arrays
import pandas as pd     			#library for managing relational (i.e. table-format) datasets
import seaborn as sns   			#for plotting and styling
import matplotlib.pyplot as plt     #help customize plots


#%matplotlib inline 				#(only if I'm using IPython Notebook)


# FILE FORMAT:
#	Strain				Gene	No_of_mutations  Phenotype	Spoligotype Lineage Province
#TB_RSA06.annotated.vcf	RVBD_1051c	1	MDR	NULL	LIN-2	EC
#TB_RSA07.annotated.vcf	RVBD_1764	885	MDR	NULL	LIN-4	EC

##########################################################################################


genes_per_strain =  pd.read_csv("../data/s23_heatmap/combined_top30.csv") # first read it in and convert it to a dataframe using pandas

#genes_per_strain.head()
genes_per_strain = genes_per_strain.pivot("Strain", "Gene", "No_of_mutations") # transform to a pivot table format, where the Strain" is the unique row, the "Gene" the unique column and the "No_of_mutations" the fill colour
fig = plt.figure(figsize=(20,20)) # the first value controls the spacing/size of the rows and the second value the columns
heatmap = sns.heatmap(genes_per_strain, cmap = "coolwarm", robust = True, square = True)
heatmap.set_title("Top 30 genes with most mutations per strain", fontsize=15)

#heatmap.get_figure().savefig('../data/s23_heatmap/heatmap.png')		# to save it as .png file


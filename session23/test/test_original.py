import pytest
from append_vcf_line_fo_filename_Study_group import annotate_vcf_with_operon

VCF_DATA = """##fileformat=VCFv4.1
##fileDate=20131031
##source="Test Data"
##reference=genome.fasta
##contig=<ID=MT_H37RV_BRD_V5,length=4411709>
##FILTER=<ID=LowCov,Description="Low Coverage of good reads at location">
##FILTER=<ID=Amb,Description="Ambiguous evidence in haploid genome">
##FILTER=<ID=Del,Description="This base is in a deletion or change event from another record">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Valid read depth; some reads may have been filtered">
##INFO=<ID=BQ,Number=1,Type=Integer,Description="Mean base quality at locus">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	G31877:Mycobacterium_tuberculosis_TKK_02_0007
MT_H37RV_BRD_V5	1524	.	G	T	12000	PASS	DP=200;BQ=38
MT_H37RV_BRD_V5	1525	.	G	T	12000	PASS	DP=200;BQ=38
MT_H37RV_BRD_V5	2051	.	G	T	12000	PASS	DP=200;BQ=38
MT_H37RV_BRD_V5	2052	.	G	T	12000	PASS	DP=200;BQ=38"""

OPERON_DATA = """Operon	Start	Stop	Length	Orientation	Average operon coverage	Number of genes in operon	Genes in operon
MT0001	1	1524	1523	+	69.2	1	MT0001
MT0009(not expressed)	11555	11692	137	-	NOT EXPRESSED		
MT0002-MT0007	2052	10828	8776	+	100.9	6	MT0002, MT0003, MT0004, MT0005, MT0006, MT0007"""

def test_filter_variants(tmpdir):
    vcf_file = tmpdir.join('test.vcf')
    vcf_file.write(VCF_DATA)
    vcf_path = str(vcf_file)
    operon_file = tmpdir.join('operons.txt')
    operon_file.write(OPERON_DATA)
    operon_path = str(operon_file)
    with tmpdir.as_cwd():
        annotate_vcf_with_operon(operon_path, vcf_path)
        output_file = tmpdir.join('operon_test.vcf')
        output_data = output_file.read()
        for var in ('1524', '2052'):
            assert "\t"+var+"\t" in output_data, "Expected variant {} to be in output data".format(var)
        for var in ('1525', '2051'):
            assert "\t"+var+"\t" not in output_data, "Expected variant {} to not be in output data".format(var)

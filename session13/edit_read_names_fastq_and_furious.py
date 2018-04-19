import gzip
import click
from fastqandfurious import fastqandfurious


@click.command()
@click.argument('data')
def change_readnames(data):
    """ Adds "\1" or "\2" to paired end read names in fastq file generated by
    Illumina Hiseq. This format is needed for input for Trans-ABySS"""

    if data.endswith('gz'):
        input_file = gzip.open(data)
    else:
        input_file = open(data)

    bufsize = 20000
    count = 0
    it = fastqandfurious.readfastq_iter(input_file, bufsize,
                                        fastqandfurious.entryfunc)
    for entry in it:
        print(type(it))
        count += 1
    print(count, "reads in", data)


if __name__ == '__main__':
    change_readnames()

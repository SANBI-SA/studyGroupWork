#!/usr/bin/env python

import click

def split_fasta(inputfilename, output_prefix, num_chunks=10):
    count = 0
    buffer = ''
    inputfile = open(inputfilename)
    index  = count + 1
    output_destinations = []
    for i in range(num_chunks):
        output_filename = '{}{}.fasta'.format(output_prefix, i+1)
        output_file = open(output_filename, 'w')
        output_destinations.append(output_file)
    for line in inputfile:
        if line.startswith('>'):
            if len(buffer) > 0:
                destination_index = count % num_chunks
                # print("destination:", destination_index)
                output_file = output_destinations[destination_index]
                output_file.write(buffer)
                buffer = ''
                count += 1
        buffer += line
    destination_index = count % num_chunks
    output_file = output_destinations[destination_index]
    output_file.write(buffer)
    count += 1
    print("final count:", count)

    for output_file in output_destinations:
        output_file.close()

@click.command()
@click.option('--num_chunks', type=int, default=10)
@click.argument('inputfilename')
@click.argument('output_prefix')
def split_fasta_cmd(inputfilename, output_prefix, num_chunks=10):
    split_fasta(inputfilename, output_prefix, num_chunks)

if __name__ == '__main__':
    split_fasta_cmd()

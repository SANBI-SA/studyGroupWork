#!/usr/bin/env python

import click

@click.command()
@click.argument('inputfilename')
@click.argument('output_prefix')
def fastasplit(inputfilename, output_prefix):
    count = 0
    buffer = ''
    inputfile = open(inputfilename)
    index  = count + 1
    outputfile = open('{}{}.fasta'.format(output_prefix, index), 'w')
    for line in inputfile:
        if line.startswith('>'):
            if len(buffer) > 0:
                outputfile.write(buffer)
                outputfile.close()
                index = count + 1
                outputfile = open('{}{}.fasta'.format(output_prefix, index), 'w')
                buffer = ''
                count = count + 1
        buffer += line
    outputfile.write(buffer)
    outputfile.close()
    print(count)

# print('hello my name is:', __name__)
if __name__ == '__main__':
    fastasplit()

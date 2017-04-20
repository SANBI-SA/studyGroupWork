#!/usr/bin/env python

import click

# example of data
# >@unitig_1847|quiver
# TGATAGACTGCTATAAACTGAGTCTAAATGA
#
# annoying FASTA variant
# > @unitig_1847|quiver
# things to watch out for:
# 1) we don't want >
# 2) we don't want the description part
# e.g. >@unitig_1987|quiver A Seabass sequence
#   - we don't want the "A Seabass sequence part"
# 3) we don't want any whitespace around the ID
# 4) we don't want funky characters like |

def line_to_id(line):
    bare_line = line[1:]  # get rid of '>'
    trimmed_line = bare_line.strip()  # remove whitespace at the ends of the line
    parts = trimmed_line.split()  # split it into words
    id_part = parts[0]  # the first part
    clean_id = id_part.replace('|','_')  # replace | with _
    return clean_id

def get_outputfile(output_prefix, id_str):
    species = 'black_soldier_fly'
    output_filename = '{}_{}_{}.fasta'.format(output_prefix, species, id_str)
    output_file = open(output_filename, 'w')
    return output_file
    
@click.command()
@click.argument('inputfilename')
@click.argument('output_prefix')
def fastasplit(inputfilename, output_prefix):
    count = 0
    buffer = ''
    inputfile = open(inputfilename)
    index  = count + 1
    for line in inputfile:
        if line.startswith('>'):
            current_id = line_to_id(line)
            if len(buffer) > 0:
                outputfile = get_outputfile(output_prefix, current_id)
                outputfile.write(buffer)
                outputfile.close()
                index = count + 1
                buffer = ''
                count = count + 1
        buffer += line
    outputfile = get_outputfile(output_prefix, current_id)
    outputfile.write(buffer)
    outputfile.close()
    print(count)

# print('hello my name is:', __name__)
if __name__ == '__main__':
    fastasplit()

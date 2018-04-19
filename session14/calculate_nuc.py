#!/usr/bin/env python

from __future__ import print_function, division
import sys
import click
from Bio import SeqIO


def parseSeq(seq):
    a_count = c_count = g_count = t_count = other_count = 0
    seq = seq.lower()
    for base in seq:
        if base == 'a':
            a_count += 1
        elif base == 'c':
            c_count += 1
        elif base == 'g':
            g_count += 1
        elif base == 't':
            t_count += 1
        else:
            other_count += 1

    results = {
        'a': a_count,
        't': t_count,
        'c': c_count,
        'g': g_count,
        'other': other_count
    }
    # another way
    # results = dict(a=a_count, c=c_count)
    return results


@click.command()
@click.argument('input_file', type=click.File())
def print_stats(input_file):
    seq_record = SeqIO.read(input_file, "fasta")

    seq = seq_record.seq

    results = parseSeq(seq)
    a_count = results['a']
    c_count = results['c']
    t_count = results['t']
    g_count = results['g']
    other_count = results['other']
    total = a_count + t_count + c_count + g_count
    gc = round((c_count + g_count) / total * 100, 2)
    at = 100 - gc

    print("Length =", len(seq))
    print('A:', a_count)
    print('C:', c_count)
    print('G:', g_count)
    print('T:', t_count)
    print('Other:', other_count)

    print('GC:', gc)
    print('AT:', at)


if __name__ == '__main__':
    print_stats()

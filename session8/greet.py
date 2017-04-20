#!/usr/bin/env python

import click

@click.command()
@click.argument("name",default="Emily")
def greet(name):
    print ("Hello:",name)

if __name__ == "__main__":
    greet()

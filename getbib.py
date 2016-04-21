import click
from gscholar import gscholar
import os
import sys
import random

def contains_duplicate(filename, cite_id):
    """
    Check for duplicates in the .bib file (filename)
    """
    flag = False
    if os.path.isfile(filename):
        with open(filename, 'r') as out:
            for line in out: 
                if cite_id in line:
                    flag = True
                    return flag 
                else:
                    pass
    return flag

@click.command()
@click.argument('query')
@click.option('-f', '--filename', default=None, type=str, help='Path to .bib file to update.')
@click.option('--allresults', is_flag=True, help='Process all of the results, rather than only the top match')
@click.option('--manual', default=None, type=str, help='Manual entry')
def _main(query, filename, allresults, manual):
    # Manual entry
    if manual:
        if contains_duplicate(manual_entry) == True:
            click.echo("Duplicate found, aborting.")
            return
        manual_id = manual.split(' ', 1)[0] + str(9) + str(random.randint(0,99)) # Use the first word + random int as the label
        with open(filename,'a') as out:
            out.write("@manual{" + manual_id + ",\n\t")
            out.write("Title = {" + manual_entry + "}}")
            out.write("\n") # such that the next item is well spaced 
        click.echo('Manual entry added successfully!')
        click.echo('    \cite{{{}}}'.format(manual_id))
        click.echo('    \citeA{{{}}}'.format(manual_id))
        return

    # Request to gscholar, encode to UTF8 (for python 2 compatibility)
    response = gscholar.query(query.encode('UTF-8'), allresults=allresults)
    response = [i.encode('UTF-8') for i in response]

    for item in response:
        # @article{nameYEARword, ... find cite_id between the first '{' and ','
        cite_id = item.split('{')[1].split(',')[0]

        if filename:
            if contains_duplicate(filename, cite_id) == True:
                click.echo('Duplicate found for {}'.format(cite_id))
            else:
                # Append bibtex output to prespecified path
                with open(filename,'a') as out:
                    out.write(item)
                    out.write("\n") # such that the next item is well spaced
                click.echo('Citation added successfully!')
                click.echo('    \cite{{{}}}'.format(cite_id))
                click.echo('    \citeA{{{}}}'.format(cite_id))
        else:
            click.echo(item)

if __name__ == "__main__":
   _main()

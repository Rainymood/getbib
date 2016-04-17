import gscholar
import os
import sys 
import random

def contains_duplicate(cite_id):
    """
    Check for duplicates in the .bib file (filename)
    """
    flag = False
    with open(filename,'r') as out:
        for line in out: 
            if cite_id in line:
                flag = True
                return flag 
            else:
                pass
    return flag 

def main(argv):
    # Set up bibtex filepath
    # filepath = "/Users/janmeppe/Dropbox/School/Master/Master Thesis/tex/"
    # filename = "master-thesis.bib"

    # Set up bibtex filepath
    global filepath
    global filename
    filepath = "<path to dir containing .bib file>" 
    filename = "<filename of .bib file>"
    os.chdir(filepath) # Change dir to filepath 

    # Manual entry
    if sys.argv[1] == "--manual":
        manual_entry = sys.argv[2]
        if contains_duplicate(manual_entry) == True:
            print "Duplicate found, aborting."
            sys.exit(2)
        with open(filename,'a') as out:
            out.write("@manual{" + sys.argv[2].split(' ', 1)[0] + str(9) + str(random.randint(0,99)) + ",\n\t") # Use the first word + random int as the label
            out.write("Title = {" + manual_entry + "}}")
            out.write("\n") # such that the next item is well spaced 
        print "Manual entry added: " + manual_entry
        sys.exit(2)

    # Get user input as query, request to gscholar and encode to UTF8
    user_arg      = sys.argv[1]
    query_unicode = gscholar.query(user_arg)
    query         = [x.encode('UTF8') for x in query_unicode]

    # @article{nameYEARword, ... find cite_id between the first '{' and ','
    cite_id = query[0].split(',', 1)[0].split('{',1)[1]

    if contains_duplicate(cite_id) == True:
        print "Duplicate found, aborting."
    else:
        # Append bibtex output to prespecified path 
        with open(filename,'a') as out:
            for item in query:
                out.write("%s" % item)
            out.write("\n") # such that the next item is well spaced 
        print "Citation added successfully!\n\cite{%s}\n\citeA{%s}" % (cite_id, cite_id)

if __name__ == "__main__":
   main(sys.argv[1:])

import gscholar
import os
import sys 

# Set up bibtex filepath
# filepath = "/Users/janmeppe/Dropbox/School/Master/Master Thesis/tex/"
# filename = "master-thesis.bib"

# Set up bibtex filepath
filepath = "<path to dir containing .bib file>" 
filename = "<filename of .bib file>"
os.chdir(filepath) # Change dir to filepath 

# Get user input as query, request to gscholar and encode to UTF8
user_arg      = sys.argv[1]
query_unicode = gscholar.query(user_arg)
query         = [x.encode('UTF8') for x in query_unicode]

# Append bibtex output to prespecified path 
with open(filename,'a') as out:
    for item in query:
        out.write("%s" % item)
    out.write("\n") # such that the next item is well spaced 

# @article{nameYEARword, ... } find cite_id between the first '{' and ','
cite_id = query[0].split(',', 1)[0].split('{',1)[1]
print "Citation added succefully!\n\cite{%s}\n\citeA{%s}" % (cite_id, cite_id)



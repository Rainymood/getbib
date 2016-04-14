
# Hello 

Getbib.py will automatically add the BiBTeX code to your specified .bib file. 

Here is a [video](https://www.youtube.com/watch?v=Qnr1v3wg96I) which showcases
getbib.py. Please don't mind my horrible english. 

# Setup

Because of time constraints I have not yet been able to make a really nice setup
file (i.e. pip installable). The output path (dir containing .bib file) and
filename (the actual .bib file) are hard-coded, which you will have to change
manually.  Copy the files to some dir you want to work from and make sure you
execute the python script from that directory. If you have any more questions
feel free to contact me. 

# Usage

    $ python getbib.py "<query>"

For example

    $ python getbib.py "Leo Breiman. Random forests. Machine Learning, 45(1):5–32, 2001."

Which results in the following output

    Citation added succefully!
    \cite{breiman2001random}
    \citeA{breiman2001random}

I personally made a bash alias which shortens this to

    $ gb "<query>"

You can do so by adding the following line to your ~/.bashrc

    alias gb = "python getbib.py"

# Thanks

I made this script by standing on the shoulders of [gscholar](https://github.com/venthur/gscholar). 





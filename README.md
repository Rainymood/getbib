
# Hello 

Getbib.py will automatically add the BiBTeX code to your specified .bib file. 

Here is a [video](https://www.youtube.com/watch?v=Qnr1v3wg96I) which showcases
getbib.py. Please don't mind my horrible english. 

# Setup

    $ git clone https://github.com/Rainymood/getbib.git
    $ cd getbib
    $ pip install -r requirements.txt
    $ python getbib.py --help

# Usage

    $ python getbib.py "<query>" -f <.bib filename>

For example:

    $ python getbib.py "Leo Breiman. Random forests. Machine Learning, 45(1):5–32, 2001." -f output.bib

    Citation added succesfully!
        \cite{breiman2001random}
        \citeA{breiman2001random}

If you want to add all of the returned citations, simply add the --allresults flag. For example:

    $ python getbib.py "Random forests" -f output.bib --allresults

	Citation added successfully!
	    \cite{breiman2001random}
	    \citeA{breiman2001random}
	Citation added successfully!
	    \cite{bosch2007image}
	    \citeA{bosch2007image}
	Citation added successfully!
	    \cite{prasad2006newer}
	    \citeA{prasad2006newer}
	Citation added successfully!
	    \cite{cutler2007random}
	    \citeA{cutler2007random}
	Citation added successfully!
	    \cite{gislason2006random}
	    \citeA{gislason2006random}
	Citation added successfully!
	    \cite{strobl2008conditional}
	    \citeA{strobl2008conditional}
	Citation added successfully!
	    \cite{strobl2009introduction}
	    \citeA{strobl2009introduction}
	Citation added successfully!
	    \cite{statnikov2008comprehensive}
	    \citeA{statnikov2008comprehensive}
	Citation added successfully!
	    \cite{lunetta2004screening}
	    \citeA{lunetta2004screening}
	Citation added successfully!
	    \cite{genuer2010variable}
	    \citeA{genuer2010variable}


I personally made a bash alias which shortens this to

    $ gb "<query>"

You can do so by adding the following line to your ~/.bashrc

    alias gb = "python getbib.py -f /Users/janmeppe/Dropbox/School/Master/Master Thesis/tex/master-thesis.bib"

# Thanks

I made this script by standing on the shoulders of [gscholar](https://github.com/venthur/gscholar). 

# Issues

  * Unicode is not handled well across python 2/3
  * Needs tests
  * Too many queries leads to a 503: Service Unavailable
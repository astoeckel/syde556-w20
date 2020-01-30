#!/bin/bash -e

# Create a random folder
DIR=$( mktemp -d )

# Copy the file we're working on to the temp directory
cp "$1.ipynb" "$DIR"

# Go to this directory
cd "$DIR"
jupyter nbconvert --to latex --template article "$1.ipynb"

# Fetch the student's name
ID=$( grep -i "Student ID:" "$1.tex" | sed 's/.*Student ID:[^0-9]*\([0-9 ]\+\).*/\1/I' )

# Change a few settings
sed -i 's/\\maketitle//' "$1.tex"
sed -i 's/section{/section*{/' "$1.tex"
sed -i 's/subsection{/subsection*{/' "$1.tex"
sed -i 's/\(\\documentclass\[\(.*\)\]{article}$\)/\1\n\n    \\usepackage{palatino}\n    \\setlength{\\parindent}{0cm}\n    \\setlength{\\parskip}{1em}\n/' "$1.tex"
sed -i 's/\\begin{Verbatim}\[\(.*\)\]/\\begin{Verbatim}[\1,fontsize=\\small]/' "$1.tex"
sed -i 's/\\geometry{.*$/\\geometry{a4paper,top=3cm,bottom=2cm,left=2.5cm,right=2.5cm}\n    \\usepackage{fancyhdr}\n    \\pagestyle{fancy}\n    \\fancyhf{}\n    \\lhead{Student ID: '"$ID"'}\n    \\rhead{\\thepage}\n/' "$1.tex"

# Execute xelatex on the file
xelatex -interaction=nonstopmode "$1" || true

# Copy the resulting PDF back and delete the temporary directory
cd -
cp "$DIR/$1.pdf" .

# Delete the temporary directory
rm -rf "$DIR"

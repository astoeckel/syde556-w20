all: \
	assignment_01/syde556_assignment_01.pdf \
	assignment_01/syde556_assignment_01_template.pdf \
	assignment_02/syde556_assignment_02.pdf \
	assignment_02/syde556_assignment_02_template.pdf \
	assignment_03/syde556_assignment_03.pdf \
	assignment_03/syde556_assignment_03_template.pdf \
	assignment_04/syde556_assignment_04.pdf \
	assignment_04/syde556_assignment_04_template.pdf

assignment_01/syde556_assignment_01.pdf: \
	syde556_assignment_preamble.tex \
	assignment_01/syde556_assignment_01.tex
	cd assignment_01 && latexmk syde556_assignment_01

assignment_01/syde556_assignment_01_template.pdf: \
	ipynb_to_pdf.sh \
	assignment_01/syde556_assignment_01_template.ipynb
	cd assignment_01 && ../ipynb_to_pdf.sh syde556_assignment_01_template

assignment_02/syde556_assignment_02.pdf: \
	syde556_assignment_preamble.tex \
	assignment_02/syde556_assignment_02.tex
	cd assignment_02 && latexmk syde556_assignment_02 && ../ipynb_to_pdf.sh syde556_assignment_02_template

assignment_02/syde556_assignment_02_template.pdf: \
	ipynb_to_pdf.sh \
	assignment_02/syde556_assignment_02_template.ipynb
	cd assignment_02 && ../ipynb_to_pdf.sh syde556_assignment_02_template

assignment_03/syde556_assignment_03.pdf: \
	syde556_assignment_preamble.tex \
	assignment_03/syde556_assignment_03.tex
	cd assignment_03 && latexmk syde556_assignment_03 && ../ipynb_to_pdf.sh syde556_assignment_03_template

assignment_03/syde556_assignment_03_template.pdf: \
	ipynb_to_pdf.sh \
	assignment_03/syde556_assignment_03_template.ipynb
	cd assignment_03 && ../ipynb_to_pdf.sh syde556_assignment_03_template

assignment_04/syde556_assignment_04.pdf: \
	syde556_assignment_preamble.tex \
	assignment_04/syde556_assignment_04.tex
	cd assignment_04 && latexmk syde556_assignment_04 && ../ipynb_to_pdf.sh syde556_assignment_04_template

assignment_04/syde556_assignment_04_template.pdf: \
	ipynb_to_pdf.sh \
	assignment_04/syde556_assignment_04_template.ipynb
	cd assignment_04 && ../ipynb_to_pdf.sh syde556_assignment_04_template

clean:
	rm -f lecture_??/*.aux
	rm -f lecture_??/*.fdb_latexmk
	rm -f lecture_??/*.fls
	rm -f lecture_??/*.log
	rm -f lecture_??/*.out
	rm -f lecture_??/*.toc
	rm -f lecture_??/*.synctex.gz
	rm -f lecture_??/*.run.xml
	rm -f lecture_??/*.blg
	rm -f lecture_??/*.bcf
	rm -f lecture_??/*.bbl
	rm -f lecture_??/*.nav
	rm -f lecture_??/*.snm

distclean: clean
	rm -f lecture_??/*.pdf
	rm -f lecture_??/*.md


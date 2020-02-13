all: \
	lecture_00/syde556_lecture_00_notes.pdf \
	lecture_00/syde556_lecture_00_slides.pdf \
	lecture_00/syde556_lecture_00_slides_distr.pdf \
	lecture_00/syde556_lecture_00_notes.md \
	lecture_01/syde556_lecture_01_notes.pdf \
	lecture_01/syde556_lecture_01_slides.pdf \
	lecture_01/syde556_lecture_01_slides_distr.pdf \
	lecture_02/syde556_lecture_02_notes.pdf \
	lecture_02/syde556_lecture_02_slides.pdf \
	lecture_02/syde556_lecture_02_slides_distr.pdf \
	lecture_03/syde556_lecture_03_notes.pdf \
	lecture_03/syde556_lecture_03_slides.pdf \
	lecture_03/syde556_lecture_03_slides_distr.pdf \
	lecture_04/syde556_lecture_04_notes.pdf \
	lecture_04/syde556_lecture_04_slides.pdf \
	lecture_04/syde556_lecture_04_slides_distr.pdf \
	lecture_05/syde556_lecture_05_notes.pdf \
	lecture_05/syde556_lecture_05_slides.pdf \
	lecture_05/syde556_lecture_05_slides_distr.pdf \
	lecture_06/syde556_lecture_06_notes.pdf \
	lecture_06/syde556_lecture_06_slides.pdf \
	lecture_06/syde556_lecture_06_slides_distr.pdf \
	lecture_07/syde556_lecture_07_notes.pdf \
	lecture_07/syde556_lecture_07_slides.pdf \
	lecture_07/syde556_lecture_07_slides_distr.pdf \


lecture_00/syde556_lecture_00_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_00/syde556_lecture_00_notes.tex
	cd lecture_00; latexmk syde556_lecture_00_notes

lecture_00/syde556_lecture_00_notes.md: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_00/syde556_lecture_00_notes.tex
	cd lecture_00; pandoc syde556_lecture_00_notes.tex -t markdown_strict -o syde556_lecture_00_notes.md

lecture_00/syde556_lecture_00_slides.pdf: \
		syde556_lecture_slides_preamble.tex \
		lecture_00/syde556_lecture_00_slides.tex
	cd lecture_00; latexmk syde556_lecture_00_slides

lecture_00/syde556_lecture_00_slides_distr.pdf: \
		lecture_00/syde556_lecture_00_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_01/syde556_lecture_01_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_01/syde556_lecture_01_notes.tex
	cd lecture_01; latexmk syde556_lecture_01_notes

lecture_01/syde556_lecture_01_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_01/syde556_lecture_01_slides.tex
	cd lecture_01; latexmk syde556_lecture_01_slides

lecture_01/syde556_lecture_01_slides_distr.pdf: \
		lecture_01/syde556_lecture_01_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_02/syde556_lecture_02_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_02/syde556_lecture_02_notes.tex
	cd lecture_02; latexmk syde556_lecture_02_notes

lecture_02/syde556_lecture_02_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_02/syde556_lecture_02_slides.tex
	cd lecture_02; latexmk syde556_lecture_02_slides

lecture_02/syde556_lecture_02_slides_distr.pdf: \
		lecture_02/syde556_lecture_02_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_03/syde556_lecture_03_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_03/syde556_lecture_03_notes.tex
	cd lecture_03; latexmk syde556_lecture_03_notes

lecture_03/syde556_lecture_03_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_03/syde556_lecture_03_slides.tex
	cd lecture_03; latexmk syde556_lecture_03_slides

lecture_03/syde556_lecture_03_slides_distr.pdf: \
		lecture_03/syde556_lecture_03_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_04/syde556_lecture_04_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_04/syde556_lecture_04_notes.tex
	cd lecture_04; latexmk syde556_lecture_04_notes

lecture_04/syde556_lecture_04_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_04/syde556_lecture_04_slides.tex
	cd lecture_04; latexmk syde556_lecture_04_slides

lecture_04/syde556_lecture_04_slides_distr.pdf: \
		lecture_04/syde556_lecture_04_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_05/syde556_lecture_05_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_05/syde556_lecture_05_notes.tex
	cd lecture_05; latexmk syde556_lecture_05_notes

lecture_05/syde556_lecture_05_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_05/syde556_lecture_05_slides.tex
	cd lecture_05; latexmk syde556_lecture_05_slides

lecture_05/syde556_lecture_05_slides_distr.pdf: \
		lecture_05/syde556_lecture_05_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_06/syde556_lecture_06_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_06/syde556_lecture_06_notes.tex
	cd lecture_06; latexmk syde556_lecture_06_notes

lecture_06/syde556_lecture_06_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_06/syde556_lecture_06_slides.tex
	cd lecture_06; latexmk syde556_lecture_06_slides

lecture_06/syde556_lecture_06_slides_distr.pdf: \
		lecture_06/syde556_lecture_06_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<

lecture_07/syde556_lecture_07_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_07/syde556_lecture_07_notes.tex
	cd lecture_07; latexmk syde556_lecture_07_notes

lecture_07/syde556_lecture_07_slides.pdf: \
		bibliography.bib \
		syde556_lecture_slides_preamble.tex \
		lecture_07/syde556_lecture_07_slides.tex
	cd lecture_07; latexmk syde556_lecture_07_slides

lecture_07/syde556_lecture_07_slides_distr.pdf: \
		lecture_07/syde556_lecture_07_slides.pdf \
		make_distr_slides.py
	./make_distr_slides.py $<


clean:
	rm -f lecture_??/*.aux
	rm -f lecture_??/*-?.cpt
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
	rm -f *.aux
	rm -f *.fdb_latexmk
	rm -f *.fls
	rm -f *.log

distclean: clean
	rm -f lecture_??/*.pdf
	rm -f lecture_??/*.md


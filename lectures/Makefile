all: \
	lecture_00/syde556_lecture_00_notes.pdf \
	lecture_00/syde556_lecture_00_slides.pdf \
	lecture_00/syde556_lecture_00_notes.md \
	lecture_01/syde556_lecture_01_notes.pdf \


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

lecture_01/syde556_lecture_01_notes.pdf: \
		bibliography.bib \
		syde556_lecture_notes_preamble.tex \
		lecture_01/syde556_lecture_01_notes.tex
	cd lecture_01; latexmk syde556_lecture_01_notes


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


filename=main

pdf:
	latex ${filename}
	bibtex ${filename}||true
	rm ${filename}.log ${filename}.aux ${filename}.out ${filename}.bbl ${filename}.blg
	dvips -t letter ${filename}.dvi
	rm ${filename}.dvi
	ps2pdf ${filename}.ps
	rm ${filename}.ps
	
remove_pdf:
	rm ${filename}.pdf

clean:
	rm ${filename}.ps ${filename}.pdf ${filename}.log ${filename}.aux ${filename}.out ${filename}.dvi ${filename}.bbl ${filename}.blg

main_bib=/Users/yoavram/Documents/library.bib
ms_bib=ms/bibtex.bib
pdf=ms/ms.pdf
md=ms/ms.md
csl=ms/evolution.csl

diagram_dot = src/model_diagram.dot
diagram_pdf = figures/model_diagram.pdf

list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
no_targets__:

$(ms_bib): $(main_bib) $(md)
	python src/getbib.py $(main_bib) $(md) $@

$(pdf): $(md) $(ms_bib) $(diagram_pdf)
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -s -S $< -o $@ --filter pandoc-crossref --filter pandoc-citeproc --bibliography=$(ms_bib) --csl $(csl) --latex-engine=xelatex --number-sections
	@open $(pdf)

$(diagram_pdf): $(diagram_dot)
	dot graph.dot -Tpdf -Kdot -ofigures/model_diagram.pdf

model_diagram: $(diagram_pdf)

bib: $(ms_bib)

build: $(pdf)

edit: $(md)
	@subl $<

read: $(pdf)
	@open $(pdf)

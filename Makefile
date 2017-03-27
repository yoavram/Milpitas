md=ms/ms.md
pdf=ms/ms.pdf
docx=ms/ms.docx
template=./ms/template.latex

main_bib=/Users/yoavram/Documents/library.bib
ms_bib=ms/bibtex.bib
citation_keys=ms/citation_keys
csl=ms/evolution.csl

diagram_dot = src/model_diagram.dot
diagram_pdf = figures/model_diagram.pdf

pandoc_opts=-r markdown+simple_tables+table_captions+yaml_metadata_block -s -S --filter pandoc-crossref --filter pandoc-citeproc --bibliography=$(ms_bib) --csl $(csl) --toc --template=$(template)

list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
no_targets__:

$(citation_keys): $(md)
	python src/get_citations.py $(md) $(citation_keys)

$(ms_bib): $(citation_keys) $(main_bib)
	python src/get_bibtex.py $(citation_keys) $(main_bib) $@

$(docx): $(md) $(ms_bib) $(diagram_pdf)
	pandoc $< -o $@ $(pandoc_opts)
	@open $(docx)

$(pdf): $(md) $(ms_bib) $(diagram_pdf)
	pandoc $< -o $@ --latex-engine=xelatex $(pandoc_opts)
	@open $(pdf)

$(diagram_pdf): $(diagram_dot)
	dot $< -Tpdf -Kdot -o$@

pdf: $(pdf)

docx: $(docx)

edit: $(md)
	@subl $<

read: $(pdf)
	@open $(pdf)

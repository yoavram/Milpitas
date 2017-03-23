from bibtexparser import load as load_bib
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import click


@click.command()
@click.argument('bibtex_filename', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.argument('markdown_filename', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.argument('output_filename', type=click.Path(file_okay=True, dir_okay=False, writable=True))
@click.option('-v/-V', '--verbose/--no-verbose', default=False)
def main(bibtex_filename, markdown_filename, output_filename, verbose):
	with open(bibtex_filename) as f:
		main_bib = load_bib(f)
	if verbose:
		print("Read {} entries from {}".format(len(main_bib.entries), bibtex_filename))

	with open(markdown_filename) as f:
		markdown = f.read()
	if verbose:
		print("Read {} lines from {}".format(markdown.count('\n'), markdown_filename))

	out_bib = BibDatabase()
	for e in main_bib.entries:
		if '@' + e['ID'] in markdown:
			out_bib.entries.append(e)
	
	if verbose:
		print("Writing {} entries to {}".format(len(out_bib.entries), output_filename))
	writer = BibTexWriter()
	with open(output_filename, 'w') as f:
	    f.write(writer.write(out_bib))


if __name__ == '__main__':
	main()
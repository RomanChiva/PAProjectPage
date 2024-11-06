import bibtexparser

# Load the BibTeX file
with open('cites.bib', 'r') as bib_file:
    bib_database = bibtexparser.load(bib_file)

# Open an output HTML file to write the formatted citations
with open('citations.html', 'w') as html_file:
    html_file.write('<section class="section" id="BibTeX">\n')
    html_file.write('<div class="container is-max-desktop content">\n')
    html_file.write('<h2 class="title">Citations</h2>\n')
    html_file.write('<ul>\n')

    # Format and write each entry as a list item
    for idx, entry in enumerate(bib_database.entries, start=1):
        author = entry.get('author', 'Unknown Author')
        title = entry.get('title', 'No Title')
        year = entry.get('year', 'n.d.')
        journal = entry.get('journal', '') or entry.get('booktitle', '')
        link = entry.get('url', '') or entry.get('doi', '')

        citation = f"[{idx}] {author}. {year}. {title}."
        if journal:
            citation += f" {journal}."
        if link:
            citation += f" <a href='{link}'>{link}</a>"
        
        html_file.write(f"<li>{citation}</li>\n")

    html_file.write('</ul>\n')
    html_file.write('</div>\n')
    html_file.write('</section>\n')

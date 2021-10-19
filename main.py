#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from fpdf import FPDF


def generatePDF(title, body):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', '', './arial.ttf', uni=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.multi_cell(185, 5, body, 0, 'J', 0, False)
    pdf.output(f"{title}.pdf").encode('utf-8', 'ignore')


def main():
    recipe_url = str(input("link da receita: "))
    html = urlopen(recipe_url)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find("h1").find(text=True)
    recipe = bs.find("div", {"class": "wg-text container"}).find_all('p')
    article_text = ''
    for line in recipe:
        article_text += '\n' + ''.join(line.findAll(text=True))

    generatePDF(title, article_text)


if __name__ == "__main__":
    main()

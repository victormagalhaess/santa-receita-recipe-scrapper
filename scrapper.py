#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from fpdf import FPDF


def log(message, style='info'):
    CRED = '\033[91m'
    CGREEN = '\033[92m'
    CEND = '\033[0m'

    if style == 'error':
        print(CRED + message + CEND)
    elif style == 'success':
        print(CGREEN + message + CEND)
    else:
        print(message)


def generatePDF(title, body):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', '', './fonts/arial.ttf', uni=True)
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.multi_cell(185, 5, body, 0, 'J', 0, False)
    pdf.output('result.pdf').encode('utf-8', 'ignore')


def scrapRecipe(recipe_url):
    html = urlopen(recipe_url)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').find(text=True)
    recipe = bs.find('div', {'class': 'wg-text container'}).find_all('p')
    return {'recipe': recipe, 'title': title}


def getArticleText(recipe):
    article_text = ''
    for line in recipe:
        article_text += '\n' + ''.join(line.findAll(text=True))
    return article_text


def getRecipe(recipe_url):
    try:
        full_recipe = scrapRecipe(recipe_url)
        recipe = full_recipe['recipe']
        title = full_recipe['title']
        article_text = getArticleText(recipe)
        generatePDF(title, article_text)
        log(f'Recipe "{title}" generated with success', 'success')
    except:
        log('An error occurred while getting the recipe', 'error')

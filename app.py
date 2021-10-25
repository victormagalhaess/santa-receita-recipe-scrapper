from flask import Flask, request, send_file
from scrapper import getRecipe
app = Flask(__name__)


@app.route("/recipe")
def scrappRecipe():
    path = './result.pdf'
    recipeUrl = request.args.get('url')
    getRecipe(recipeUrl)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000, debug=False)

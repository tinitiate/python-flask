## >---
## >title: Python Flask Jinja Blocks
## >metadata:
## >    description: 'Python Templating Jinja engine Blocks'
## >    keywords: 'Python Templating Jinja Blocks, code examples, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: python-jinja-blocks
## >slug: python/flask/jinja-blocks
## >---

## >## Python Flask Jinja Blocks

## ># Demomstration of basic Jinja template with Blocks
## >* BLOCKS in JINJA are callable JINJA code from another HTML file.
## >* A base HTML template can have BLOCK references and the CODE of that BLOCK
## >  is in another HTML file.
## >* Here we have the web-template in the file "/flaskApp/templates/jinja-block.html"
## >  it contains the BLOCK DEFINITION and the  "/flaskApp/templates/jinja-block-caller.html"
## >  calls the jinja-block.html using the "extends" keyword.

## >```python
from flask import Flask, render_template
from app import app

app = Flask(__name__)

# We will route the ROOT "/" and the "index.html" to the same function
# index()
@app.route('/')
@app.route('/index')
def index():
    
    # return render_template('jinja-basics.html', title, body, list_data)
    return render_template('jinja-block.html')

    
if __name__ == '__main__':
   app.run(debug = True)

## >```
## >---
## >title: Python Flask Jinja
## >metadata:
## >    description: 'Python Templating Jinja engine'
## >    keywords: 'Python Templating Jinja engine, code examples, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: python-jinja
## >slug: python/flask/jinja
## >---

## >## Python Flask Jinja
## >* Jinja is a HTML template engine for Python
## >* A **TEMPLATE ENGINE** is a WEB LAYOUT with basic HTML page layout, 
## >  it may include various CSS and JS scripts as well.
## >* It is useful when we have a same layout for many pages, but different 
## >  content in each of the pages.

## ># Demomstration of basic Jinja template with variables and lists
## >* Here we have the web-template in the file "/flaskApp/templates/jinja-basics.html"
## >* JINJA is invoked by the "render_template" library called.

## >```python
from flask import Flask, render_template
from app import app

app = Flask(__name__)

# We will route the ROOT "/" and the "index.html" to the same function
# index()
@app.route('/')
@app.route('/index')
def index():
    
    # Create a data that is supplied to the Jinja Web page template,
    # The template is located in '/flaskApp/templates/jinja-basics.html'
    
    # Variables to hold data
    # Data in a variable
    title = 'Tinitiate JINJA demonstration'
    
    # Data in a List
    list_data = ['Python', 'Flask' ,'Jinja']
    
    # Data in a Dictionary
    body = { 'heading':'Welcome to Tinitiate Jinja Demo'
            ,'para':'This is JINJA template demo, where data is passed from a Variable "title", a List "head" and a dictionary "body"'}    
    
    
    # return render_template('jinja-basics.html', title, body, list_data)
    return render_template('jinja-basics.html',**locals())

    
if __name__ == '__main__':
   app.run(debug = True)

## >```
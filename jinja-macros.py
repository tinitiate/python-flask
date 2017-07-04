## >---
## >title: Python Flask Jinja macros
## >metadata:
## >    description: 'Python Jinja Templating engine macros'
## >    keywords: 'Python Jinja Templating macros, jinja functions, code examples, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: python-jinja-macros
## >slug: python/flask/jinja-macros
## >---

## ># Jinja template with macros
## >* JINJA macros are same as functions or methods in python, They accept 
## >  parameters and are re-usable code blocks, Declare/Define once and reuse 
## >  many times.
## >* Here we have the web-template in the file "/flaskApp/templates/jinja-macros.html"
## >* The HTML that calls the MACROS is the "jinja-macros-caller.html"
## >* The MACROS we have are a "<p>" tag in red background and white text color,
## >  called red_box and a DROP DOWN named "html_dropdown".


## >```python
from flask import Flask, render_template
from app import app

app = Flask(__name__)

# We will route the ROOT "/" and the "index.html" to the same function
# index()
@app.route('/')
@app.route('/index')
def index():
    
    l_drop_down_data = {'mango':'MANGO','apple':'APPLE','kiwi':'KIWI','plum':'PLUM'}
    l_data = "Welcome to TINITIATE PYTHON FLASK JINJA TUTORIALS"
    l_mdd_data = [{'mango':'MANGO','apple':'APPLE','kiwi':'KIWI','plum':'PLUM'},
                  {'kale':'KALE','spinach':'SPINACH','tomato':'TOMATO','carrot':'CARROT'},
                  {'football':'FOOTBALL','cricket':'CRICKET','baseball':'BASEBALL'}]

    return render_template('jinja-macros-caller.html', p_data=l_data, p_dd_data=l_drop_down_data, p_mdd_data=l_mdd_data)

    
if __name__ == '__main__':
   app.run(debug = True)

## >```

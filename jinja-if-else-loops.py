## >---
## >title: Python Flask Jinja If Else Conditional Statement and Loops
## >metadata:
## >    description: 'Python Templating Jinja engine If Else Conditional Statement and Loops'
## >    keywords: 'Python Templating Jinja If Else Conditional Statement, Jinjs for Loop, code examples, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: python-jinja-if-else-loop
## >slug: python/flask/jinja-if-else-loop
## >---

## ># Demomstration of Jinja template with If Else conditional statements and Loops
## >* Here we have the web-template in the file "/flaskApp/templates/jinja-if-else.html"
## >* JINJA is invoked by the "render_template" library called.
## >* Here we demonstrate the IF ELSE statement implemented in the TEMPLATE

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
    l_language = 'PYTHON'
    
    # Data in a List
    l_topics = ['Python', 'Flask' ,'Jinja']
    
    
    # return render_template('jinja-basics.html', title, body, list_data)
    return render_template('jinja-if-else-loops.html'
                           ,l_language = l_language
                           ,l_topics = l_topics)



if __name__ == '__main__':
   app.run(debug = True)

## >```
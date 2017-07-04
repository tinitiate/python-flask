## >---
## >title: Python Flask URL binding
## >metadata:
## >    description: 'Python Flask URL binding is used to bind a URL to a function'
## >    keywords: 'Python flask, redirect(), url_for() routing URL binding, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: URL-binding
## >slug: python/flask/url-binding
## >---

## >## Python Flask URL bindings
## >* URL bindings enable redirecting URL to any desired function in routing
## >* Advantages of this are:
## >* Redirect a URL to another URL
## >  A function say the "localhost:5000/index" (index function) 
## >  is changed to "localhost:5000/welcome", at a later phase in the project, 
## >  then its very easy to redirect all requests, coming to 
## >  localhost:5000/index to localhost:5000/welcome
## >* This can be achieved using the url_for("welcome") function
## >* Dynamically build a URL for a specific function.

## >```python
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# This is the home-page or the "localhost:5000"
@app.route("/")
def home():
# * Now open the localhost:5000
    return "<h4>Welcome to the Tinitiate HOME</h4>"
#   This will display the following message: "Welcome to the Tinitiate HOME"


# Creating a Routes    
# The following will create a static page
@app.route("/topic")
def topic():
    return "<h4>Welcome to the TOPIC page</h4>"
# * Now open the localhost:5000/topic
#   This will display the following message: "Welcome to the TOPIC page"

    
# The following will create a static page
@app.route("/section")
def section():
    return "<h4>Welcome to the SECTION page</h4>"
# * Now open the localhost:5000/section
#   This will display the following message: "Welcome to the SECTION page"


# Create a URL_TO call for redirection of TOPIC and SECTION functions
# This function uses the url_for() for redirection
# Upon entering the URL localhost:5000/goto/section, 
# will take the page to localhost:5000/section
# AND
# Upon entering the URL localhost:5000/goto/topic, 
# will take the page to localhost:5000/topic
@app.route('/goto/<name>')
def goto(name):
   if name =='topic':
      return redirect(url_for('topic'))
   elif name =='section':
      return redirect(url_for('section'))


# URL Binding with parameters     
#  
# Creating a variable URL route
# The following will create a page to display if the given number is 
# ODD or EVEN displays in the page:
@app.route('/even_or_odd/<num>')
def even_or_odd(num):
    
    if(int(num)%2 == 0):
        return "Even or ODD: <h4>" + str(num) + " is EVEN </h4>"
    else:
        return "<h4>Even or ODD: " + str(num) + " is ODD </h4>"


# Create a URL_TO call for redirection
# This function uses the url_for() redirection
# Upon entering the URL localhost:5000/math/ANY_NUMBER, 
# will take the page to localhost:5000/even_or_odd/ANY_NUMBER
@app.route('/math/<value>')
def math(value):
   return redirect(url_for('even_or_odd',num = value))

        
if __name__ == '__main__':
   app.run(debug = True)
## >```

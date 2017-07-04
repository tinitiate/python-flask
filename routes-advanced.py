## >---
## >title: Python Flask routing advanced concepts
## >metadata:
## >    description: 'python flask routing advanced features'
## >    keywords: 'Python flask, routing advanced features, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: routing-advanced
## >slug: python/flask/routing-advanced
## >---

## >## Python Flask routing advanced features
## >* Routing is the method to display different content for every URL folder
## >* The "home page" localhost:5000, displays the default message
## >* Save the below file as `routes-advanced.py`
## >* At the command prompt run the program `python routes-advanced.py`

## >```python
from flask import Flask, render_template
app = Flask(__name__)

# This is the home-page or the "localhost:5000"
@app.route("/")
def home():
# * Now open the localhost:5000
    return "<h4>Welcome to the Tinitiate HOME</h4>"
#   This will display the following message: "Welcome to the Tinitiate HOME"


# Creating Multiple Routes    
# The following will create another page
@app.route("/topic")
def topic():
    return "<h4>Welcome to the TOPIC page</h4>"
# * Now open the localhost:5000/topic
#   This will display the following message: "Welcome to the TOPIC page"
    

# The following will create another page:
@app.route("/section")
def section():
    return "<h4>Welcome to the SECTION page</h4>"
# * Now open the localhost:5000/section
#   This will display the following message: "Welcome to the SECTION page"



    
if __name__ == '__main__':
   app.run(debug = True)    
## >```

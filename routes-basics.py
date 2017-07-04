## >---
## >title: Python Flask routing basics
## >metadata:
## >    description: 'python flask routing basics'
## >    keywords: 'Python flask, routing basics, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: routing
## >slug: python/flask/routing
## >---

## >## Python Flask routing
## >* Routing is the method to display different content for every URL folder
## >* The "home page" localhost:5000, displays the default message
## >* Save the below file as `routes-basics.py`
## >* At the command prompt run the program `python routes-basics.py`
## >* Now open the localhost:5000/section
## >  This will display the following message: "Welcome to the SECTION page"

## >```python
from flask import Flask, render_template
app = Flask(__name__)

# Using the route decorator, we add a new webpage, "section" under the localhost
@app.route("/section")
def section():
    return "<h4>Welcome to the SECTION page</h4>"
# * Now open the localhost:5000/section
#   This will display the following message: "Welcome to the SECTION page"


# Creating Multiple Routes   
# The following will create another page:
@app.route("/topic")
def topic():
    return "<h4>Welcome to the TOPIC page</h4>"
# * Now open the localhost:5000/topic
#   This will display the following message: "Welcome to the TOPIC page"    


# The following will create another page:
@app.route("/newpage")
def newpage():
    return "<h4>Welcome to the NEW-PAGE page</h4>"
# * Now open the localhost:5000/newpage
#   This will display the following message: "Welcome to the NEW-PAGE page"



if __name__ == '__main__':
   app.run(debug = True)    
## >```

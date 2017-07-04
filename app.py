## >---
## >title: Python Flask coding basics
## >metadata:
## >    description: 'python flask getting started and writing code'
## >    keywords: 'Python flask, getting started, where to begin, example code, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: basics
## >slug: python/flask/basics
## >---

## >## Python Flask getting started
## >* The objective of this program is to get started and create a simple page 
## >* Step 1. Install flask using `pip install flask`
## >* Step 2. Create a project folder say, c:\tinitiate
## >* Step 3. in the project folder create the app.py file, mentioned below. 

## >## Python Flask getting started with code
## >* The objective of this program is to get started and create a simple page 
## >* Step 1. Save the follwing code as app.py
## >* Step 2. Go to the folder of the project at the command prompt 
## >* Step 3. Run python app.py
## >* Step 4. open a browser and at the address bar localhost:5000
## >* Step 5. in the browser you should be seeing
## >   "Welcome to Tinitiate.com Python Flask free tutorials"

## >```python
from flask import Flask #, render_template

app = Flask(__name__)

# Routing is passing the control of the website for different folders,
# The root folder or "/" is the index.html file
# Using decorators to 
@app.route("/")
def main():
    return "<h4>Welcome to Tinitiate.com Python Flask free tutorials</h4>"
    

if __name__ == "__main__":
    app.run()

## >```
    
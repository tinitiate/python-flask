## >---
## >title: Python Flask Cookies
## >metadata:
## >    description: 'python flask cookies code examples'
## >    keywords: 'Python flask, cookies, example code, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: cookies
## >slug: python/flask/cookies
## >---

## >## Python Flask Cookies
## >* 

## >```python
from flask import Flask

app = Flask(__name__)

# Routing is passing the control of the website for different folders,
# The root folder or "/" is the index.html file
# Using decorators to 
@app.route("/")
def main():
    return "<h4>Welcome to Tinitiate.com Python Flask free tutorials</h4>"
    

if __name__ == "__main__":
   app.run(debug = True)

## >```
    
## >---
## >title: Python HTML Forms
## >metadata:
## >    description: 'Python Flask HTML forms'
## >    keywords: 'Python Flask, HTML forms, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: HTML-forms
## >slug: python/flask/HTML-forms
## >---

## >## Python HTML forms
## >* In this program we demonstrate using Python flask to work with HTML 
## >  Forms and form elements.
## >* Get and set values into HTML form elements check box, drop down box, 
## >  combo box, text box, button, text area.
## >* Reading from and to the HTML control.

## >```
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

# Create a FORM on the homepage, 
# Here we apply multiple form controls to see examples for various controls
@app.route('/')
def index():
    return """<html>
   <body>

        <h4>Python Flask Read from </h4>
        <form action = "http://localhost:5000/tables" method = "post">
            <select name="Programming">
                <option value="Python">Python</option>
                <option value="Java">Java</option>
                <option value="C++">C++</option>
                <option value="C#">C#</option>
            </select>
        </form>
        
      
   </body>
</html>"""


# This method is called by both the forms, and for POST and GET the data will 
# be called / received as per POST or GET.
@app.route('/getdata',methods = ['POST', 'GET'])
def getData():
    if request.method == 'POST':
        num = request.form['num_box']
  
        l_mul_table = ""
        for c1 in range(10):
            l_mul_table = l_mul_table + '<br>'\
                        + str(num) + " X " \
                        + str(c1+1) + " = " \
                        + str(int(num)*(c1+1))
            
        return "<h4>Welcome to the " + num + " Table page by POST method</h4> <br> " + l_mul_table
        
    else:
        num = request.args.get('num_box')
  
        l_mul_table = ""
        for c1 in range(10):
            l_mul_table = l_mul_table + '<br>' + str(num) + " X " + str(c1+1) + " = " + str(int(num)*(c1+1))
            
        return "<h4>Welcome to the " + num + " Table page by GET method</h4> <br> " + l_mul_table
        
    # * This will route the webpage to localhost:5000/tables

if __name__ == '__main__':
   app.run(debug = True)

## >```
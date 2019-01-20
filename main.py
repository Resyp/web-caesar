from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/add" method="POST">
      ####Two inputs####
       <label>
            Rotate By:
           <input type="text" name="rot"/>
        </label>
        
        <input type="textarea" name="text"/>
    ####The form uses the POST method.
    There are two inputs: a regular input with type="text" and a textarea.
    Set name="rot" on the input element and name="text" on the textarea.
    Has a label on the input element that looks something like the one in the screenshot above.
    The input element has the default value of 0.
    Has a submit button.####

    </body>
</html>
"""












@app.route("/")
def index():
    #TODO return form variable
    return "Hello World"

app.run()
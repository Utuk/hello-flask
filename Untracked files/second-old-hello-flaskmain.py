from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
#in <form action> tag, delete method when using GET 
form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post"> 
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""



@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST']) #change method to GET for get request
def hello():
    first_name = request.form['first_name'] #change request to this when using GET = request.args.get('first-name')
    return '<h1> Hello, ' + first_name + '</h1>'
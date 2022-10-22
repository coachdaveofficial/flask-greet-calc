from flask import Flask, request

app = Flask(__name__)
app.debug = True;
FlASK_DEBUG = 1


@app.route('/welcome')
def welcome():
    """Return welcome"""

    html = '<html><body><h1>Welcome</h1></body></html>'
    return html

@app.route('/welcome/home')
def welcome_home():
    """Return welcome home"""

    html = '<html><body><h1>Welcome Home</h1></body></html>'
    return html

@app.route('/welcome/back')
def welcome_back():
    """Return welcome back"""

    html = '<html><body><h1>Welcome Back</h1></body></html>'
    return html
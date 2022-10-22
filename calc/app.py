# Put your app in here.
from random import randint
from flask import Flask, request, render_template
import operations
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "LEAVEIT"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows calculation form"""
    return """
    <h1>Calculate</h1>
    <form method="POST">
      <label for="operations">Choose an operation</label>
        <select id="operations" name="operations">
            <option value="add">add</option>
            <option value="sub">subtract</option>
            <option value="mult">multiply</option>
            <option value="div">divide</option>
        </select>
        <label>Insert two numbers</label>
            <input type="text" placeholder="Value #1" name="value-1">
            <input type="text" placeholder="Value #2" name="value-2">
        <input type="submit">
    </form>
  """

@app.route('/', methods=["POST"])
def form_results():
    """Shows calculation"""

    try:
        value_1 = float(request.form['value-1'])
        value_2 = float(request.form['value-2'])
    except ValueError:
        return """
        <h1>Error</h1> 
        <h3>Please input number characters only (example: 1, 2, 3 etc.)</h3>
        """
    op = request.form["operations"]
    func = getattr(operations, op)
    result = func(value_1, value_2)
    return f"""
    <h1>Calculated</h1>
    <h2>{result}</h2>
  """

@app.route('/<operation>')
def results(operation):
    """Shows calculation"""

    try:
        value_1 = float(request.args["a"])
        value_2 = float(request.args["b"])
    except ValueError:
        return """
        <h1>Error</h1> 
        <h3>Please input number characters only (example: 1, 2, 3 etc.)</h3>
        """
    func = getattr(operations, operation)
    result = func(value_1, value_2)
    return f"""
    <h1>Calculated</h1>
    <h2>{result}</h2>
    
  """

# @app.route('/lucky/')
# def lucky_number():
#     num = randint(1,20)
#     return render_template('lucky.html', lucky_num=num)



if __name__ == "__main__":
    app.run(port=8000, debug=True)
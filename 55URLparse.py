# 23rd April 2023
# Web development(backend) using flask

from flask import Flask  # ModuleNotFoundError: No module named 'flask'
# install using pycharm (clicking on the red bulb)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, Chandra!</h1>'
            '<h2>One more item</h2>'
            '<img src="https://1000logos.net/wp-content/uploads/2020/08/Python-Logo-768x480.png" width=200>'
            '<iframe src="https://giphy.com/embed/YRVP7mapl24G6RNkwJ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/moodman-YRVP7mapl24G6RNkwJ">via GIPHY</a></p>')
    # return '<h1 style="text-align: center">Hello, Chandra!</h1>' \
    #         <This is a new paragraph, a new line of code \
    #         <p>This is a paragraph</p>')

def make_bold(function_name):
    def wrapper_function():
        return '<b>'+function_name()+'</b>'
    return wrapper_function

def make_emp(function_name):
    def wrapper_function():
        return '<em>'+function_name()+'</em>'
    return wrapper_function

@app.route("/bye")
@make_bold
@make_emp
def bye():
    return "Bye!"
#    return "<p>Bye, Bye!</p>"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"




# Below lines of code makes easy to launch the browser(by click run this file)
# Else you would need to go @ cmd prompt. Export py file/app and run flask

if __name__ == '__main__':
    #app.run()  # without debug mode
    app.run(debug=True)  # debug mode

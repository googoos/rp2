# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators  to link the function to an url
@app.route("/")
@app.route("/hello")

# define the view using a function, wich return a string
def hello_world():
    return("Hello, world!")

# start the development server using the run() method
if __name__ == "__main__":
    app.run()

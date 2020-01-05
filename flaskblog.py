# ritz363
from flask import Flask

app = Flask(__name__)#initializes app

@app.route("/")#first decorator for page1
@app.route("/page1")#second decorator for page 1
def page1():
	return "<h1>This is Page 1!!!</h1>\n\n<h4>Go to 'localhost:5000/page2' for page 2</h4>\n<i>ritz363</i>"#text for page 1

@app.route("/page2")#decorator for page2
def page2():
	return "<h1>This is Page 2!!!</h1>\n\n<h4>Go to 'localhost:5000/page1' for page 1</h4>\n<i>ritz363</i>"#text for page 2

if __name__ == '__main__':#allows for debugging and to run program without environmental variables
	app.run(debug=True)
